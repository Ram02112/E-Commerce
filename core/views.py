from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from core.models import Address, CartOrder, CartOrderItems, Products,Vendor
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib import messages
from userauths.forms import ProfileForm, VendorForm

from userauths.models import ContactUs, Profile
# Create your views here.

def index(request):
  products = Products.objects.filter(product_status="published",featured = True)

  context = {
    "products":products
  }
  return render(request, 'index.html',context)


def vendor_list_view(request):
  vendor = Vendor.objects.all()

  context = {
    "vendor" : vendor
  }

  return render(request,"core/vendorlist.html",context)


def vendor_details_view(request,vendor_id):
  vendor = Vendor.objects.get(vendor_id = vendor_id)
  products = Products.objects.filter(product_status = "published",vendor = vendor)
  context = {
    "vendor":vendor,
    "products" : products
  }

  return render(request,"core/vendordetails.html",context)



def search_view(request):
  query = request.GET.get('q')

  products = Products.objects.filter(title__icontains=query).order_by("-date")

  context = {
    "products":products,
    "query" : query 
  }

  return render(request,"core/search.html",context)


def add_to_cart_view(request):
    cart_product = {
        str(request.GET['id']): {
            'title': request.GET['title'],
            'qty': request.GET['qty'],
            'price': request.GET['price'],
            'image':request.GET['image']
        }
    }

    if 'cart_data_obj' in request.session:
        cart_data = request.session['cart_data_obj']
        if str(request.GET['id']) in cart_data:
            cart_data[str(request.GET['id'])]['qty'] = int(request.GET['qty'])
        else:
            cart_data.update(cart_product)
    else:
        cart_data = cart_product

    request.session['cart_data_obj'] = cart_data

    return JsonResponse({
        "data": request.session['cart_data_obj'],
        'totalcartitems': len(request.session['cart_data_obj'])
    })



def cart_view(request):
    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        cart_data_obj = request.session['cart_data_obj']
        cart_data_items = cart_data_obj.items()
        for product_id, item in cart_data_items:
            cart_total_amount += int(item['qty']) * float(item['price'])
        return render(request, "core/cart.html", {
            "cart_data_items": cart_data_items,
            'totalcartitems': len(cart_data_obj),
            'cart_total_amount': cart_total_amount
        })
    else:
        return render(request, 'core/emptycart.html')


def delete_item_from_cart(request):
    product_id = request.GET.get('id')
    if 'cart_data_obj' in request.session:
        cart_data_obj = request.session.get('cart_data_obj', {})
        if product_id in cart_data_obj:
            del cart_data_obj[product_id]
            request.session['cart_data_obj'] = cart_data_obj

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for item in cart_data_obj.values():
            cart_total_amount += int(item['qty']) * float(item['price'])

    context = {
        "cart_data": cart_data_obj,
        "totalcartitems": len(cart_data_obj),
        'cart_total_amount': cart_total_amount
    }

    cart_list_html = render_to_string('core/async/cart-list.html', context)

    return JsonResponse({
        "data": cart_list_html,
        "totalcartitems": len(cart_data_obj),
        "cart_total_amount": cart_total_amount
    })





def update_cart(request):
    product_id = request.GET.get('id')
    product_qty = request.GET.get('qty')
    if 'cart_data_obj' in request.session:
        cart_data_obj = request.session.get('cart_data_obj', {})
        if product_id in cart_data_obj:
            cart_data_obj[product_id]['qty'] = product_qty
            request.session['cart_data_obj'] = cart_data_obj

    cart_total_amount = 0
    if 'cart_data_obj' in request.session:
        for item in cart_data_obj.values():
            cart_total_amount += int(item['qty']) * float(item['price'])

    context = {
        "cart_data": cart_data_obj,
        "totalcartitems": len(cart_data_obj),
        'cart_total_amount': cart_total_amount
    }

    cart_list_html = render_to_string('core/async/cart-list.html', context)

    return JsonResponse({
        "data": cart_list_html,
        "totalcartitems": len(cart_data_obj),
        "cart_total_amount": cart_total_amount
    })

@login_required
def checkout_view(request):
    cart_total_amount= 0
    total_amount = 0

    if 'cart_data_obj' in request.session:
        for product_id,item in request.session['cart_data_obj'].items():
            total_amount += int(item['qty']) * float(item['price'])
        order = CartOrder.objects.create(
            user = request.user,
            price = total_amount
        )

        for product_id,item in request.session['cart_data_obj'].items():
            cart_total_amount += int(item['qty']) * float(item['price'])
            cart_order_items = CartOrderItems.objects.create(
                order = order,
                invoice_number = "INVOICE_NO_" + str(order.id),
                item = item['title'],
                image = item['image'],
                quantity = item['qty'],
                price = item['price'],
                total = float(item['qty'])* float(item['price'])
            )
        

    host = request.get_host()
    paypal_dict = {
        'business':settings.PAYPAL_RECIEVER_EMAIL,
        'amount': cart_total_amount,
        'item_name':'order-item-no-'+ str(order.id),
        'invoice':'INVOICE_NO_'+str(order.id),
        'currency_code':'USD',
        'notify_url':'http://{}{}'.format(host,reverse('core:paypal-ipn')),
        'return_url':'http://{}{}'.format(host,reverse('core:payment-complete')),
        'cancel_url':'http://{}{}'.format(host,reverse('core:payment-failed')),
    }
    paypal_payments_button = PayPalPaymentsForm(initial =paypal_dict)
    cart_total_amount = 0
    try:
        active_address = Address.objects.get(user=request.user,status = True)
    except:
        messages.warning(request,"Only one address can be default")
    context = {
            "cart_data_obj":request.session['cart_data_obj'],
            'total_cart_items':len(request.session['cart_data_obj']),
            'cart_total_amount':cart_total_amount,
            'paypal_payments_button':paypal_payments_button,
            "active_address":active_address
        }
        
    return render(request,"core/checkout.html",context)
    

@login_required
def payment_complete_view(request):
    cart_total_amount = 0

    if 'cart_data_obj' in request.session:
        for product_id,item in request.session['cart_data_obj'].items():
            cart_total_amount +=int(item['qty']) * float(item['price'])
    return render(request,'core/paymentcomplete.html',{
            "cart_data_obj":request.session['cart_data_obj'],
            'total_cart_items':len(request.session['cart_data_obj']),
            'cart_total_amount':cart_total_amount
        })
@login_required
def payment_failed_view(request):
    return render(request,'core/paymentfailed.html')


@login_required
def customer_dashboard(request):
    orders = CartOrder.objects.filter(user=request.user).order_by("-id")
    context = {
        "orders":orders
    }
    return render(request,"core/orderhistory.html",context)


def order_details(request,id):
    order = CartOrder.objects.get(user=request.user,id=id)
    products = CartOrderItems.objects.filter(order=order)

    context = {
        "products":products
    }

    return render(request,"core/order-details.html",context)


def render_address(request):
    orders = CartOrder.objects.filter(user=request.user).order_by("-id")
    address = Address.objects.filter(user = request.user)

    if request.method == "POST":
        address = request.POST['address']

        new_address = Address.objects.create(
            user = request.user,
            address = address
        )
        messages.success(request,"Address added successfully")
        return redirect("userauths:account")


    context = {
        "orders":orders,
        "address": address
    }
    return render (request,"core/address.html",context)


def make_address_default(request):
    id = request.GET['id']
    Address.objects.update(status=False)
    Address.objects.filter(id=id).update(status=True)
    return JsonResponse({"boolean":True})


def render_security(request):
    orders = CartOrder.objects.filter(user=request.user).order_by("-id")
    profile = Profile.objects.get(user=request.user)

    context = {
        "profile":profile,
        "orders":orders
    }


    return render(request,"core/security.html",context)


def render_contact(request):
    return render(request,"core/support.html")


def ajax_contact(request):
    user_name = request.GET['user_name']
    email = request.GET['email']
    phone = request.GET['phone']
    subject = request.GET['subject']
    message = request.GET['message']

    contact = ContactUs.objects.create(
        user_name = user_name,
        email = email,
        phone = phone,
        subject = subject,
        message = message
    )

    context = {
        "bool" :True,
        "message":"Message sent successfully"
    }
    return JsonResponse({"data":context})



def profile_update(request):
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,"Profile Updated successfully")
            return redirect("core:dashboard")
    else:
        form= ProfileForm()
    context ={
      "form":form
    }
    return render(request,"core/useredit.html",context)


