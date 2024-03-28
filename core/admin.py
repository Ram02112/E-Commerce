from django.contrib import admin
from core.models import Products,Category,Vendor,CartOrder,CartOrderItems,Address


class ProductAdmin(admin.ModelAdmin):
  list_display = ['user','title','product_image','price','featured','product_status']


class CategoryAdmin(admin.ModelAdmin):
  list_display = ['title','category_image']

class VendorAdmin(admin.ModelAdmin):
  list_display = ['title','vendor_image']

class CartOrderAdmin(admin.ModelAdmin):
  list_editable = ['paid_status','product_status']
  list_display = ['user','price','paid_status','order_date','product_status']

class CartOrderItemsAdmin(admin.ModelAdmin):
  list_display = ['order','invoice_number','item','image','quantity','price','total']

class AddressAdmin(admin.ModelAdmin):
  list_editable = ['address','status']
  list_display = ['user','address','status']


admin.site.register(Products,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(CartOrder,CartOrderAdmin)
admin.site.register(CartOrderItems,CartOrderItemsAdmin)
admin.site.register(Address,AddressAdmin)