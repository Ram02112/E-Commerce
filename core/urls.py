from django.urls import include, path 
from core import views
app_name = 'core'

urlpatterns = [
  path('',views.index,name="index"),
  path('vendor/',views.vendor_list_view,name="vendor-list"),
  path('vendors/<vendor_id>/',views.vendor_details_view,name="vendor-details"),
  path('search/',views.search_view,name = "search"),
  path('add-to-cart/',views.add_to_cart_view,name="add-to-cart"),
  path("cart/",views.cart_view,name="cart"),
  path("delete-from-cart/",views.delete_item_from_cart,name="delete-from-cart"),
  path("update-cart/",views.update_cart,name="update-cart"),
  path("checkout/",views.checkout_view,name="checkout"),
  path('payment-complete/',views.payment_complete_view,name='payment-complete'),
  path('payment-failed/',views.payment_failed_view,name='payment-failed'),
  path('paypal/',include('paypal.standard.ipn.urls')),
  path("dashboard/",views.customer_dashboard,name="dashboard"),
  path('dashboard/order/<int:id>',views.order_details,name="order-details"),
  path('address/',views.render_address,name="address"),
  path("make-default-address/",views.make_address_default,name="make-default-address"),
  path("profile-security/",views.render_security,name="profile-security"),
  path("support/",views.render_contact,name="support"),
  path("ajax-contact-form/",views.ajax_contact,name="ajax-contact-form"),
  path("editprofile/",views.profile_update,name="editprofile"),
   
]