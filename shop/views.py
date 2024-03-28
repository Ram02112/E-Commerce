from django.shortcuts import render
from core.models import Products,Category
# Create your views here.

def baby_products(request):
  category_id = "category1da5332cde"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/babyproducts.html',context)

def beauty(request):
  category_id = "categoryfga3a13a2b"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/beauty.html',context)

def books(request):
  category_id = "categorye3fcdc212a"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/books.html',context)

def branded(request):
  category_id = "categoryha1hg2a4g1"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/branded.html',context)

def clothing(request):
  category_id = "category5a4ec41b1a"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)



  context = {
    "products":products,
  }
  return render(request,'shop/clothing.html',context)

def dvd(request):
  category_id = "category12g351che2"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/dvd.html',context)


def electronics(request):
  category_id = "categorydccheb1fbf"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/electronics.html',context)

def furniture(request):
  category_id = "category44ge55b23d"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/furniture.html',context)

def games(request):
  category_id = "categoryebhaffbcc4"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/games.html',context)

def gardening(request):
  category_id = "categorybdf2c4abfh"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/gardening.html',context)

def giftcards(request):
  category_id = "categoryde124ea53d"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/giftcards.html',context)

def healthcare(request):
  category_id = "category4ff4decacc"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/healthcare.html',context)

def industrial(request):
  category_id = "categoryg5gee1hd52"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/industrial.html',context)

def jewellery(request):
  category_id = "category3253h4be3b"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/jewellery.html',context)

def kitchen(request):
  category_id = "categoryb5ge5ch1b1"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/kitchen.html',context)

def luxury(request):
  category_id = "categoryf2c5ccbga3"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/luxury.html',context)

def musical(request):
  category_id = "categorydf41fa2a54"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/musical.html',context)

def office(request):
  category_id = "categoryhebfaa5351"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/office.html',context)

def outdoor(request):
  category_id = "categoryfa2444dh5f"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/outdoor.html',context)

def petcare(request):
  category_id = "categoryadde1g5dde"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/petcare.html',context)


def sports(request):
  category_id = "category15a45dhac4"
  category = Category.objects.get(category_id=category_id)
  products = Products.objects.filter(category=category)
  
  context = {
    "products":products
  }
  return render(request,'shop/sports.html',context)


