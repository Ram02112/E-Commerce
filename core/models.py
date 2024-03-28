from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User


STATUS_CHOICE = (
  ("processing","Processing"),("shipped","Shipped"),("delivered","Delivered")
)
STATUS = (
  ("draft","Draft"),("disabled","Disabled"),("rejected","Rejected"),("in_review","In_Review"),("published","Published")
)




def user_directory_path(instance,filename):
  return 'user_{0}/{1}'.format(instance.user.id,filename)


# Create your models here.
class Category(models.Model):
  category_id = ShortUUIDField(unique=True,length = 10,max_length = 30,prefix = "category",alphabet="abcdefgh12345")
  title = models.CharField(max_length = 100)
  image = models.ImageField(upload_to="category")

  class Meta:
    verbose_name_plural = "categories"

  def category_image(self):
    return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))
  
  def __str__(self):
    return self.title
  

class Vendor(models.Model):
  vendor_id = ShortUUIDField(unique=True,length = 10,max_length = 30,prefix = "vendor",alphabet="abcdefgh12345")
  title = models.CharField(max_length = 100)
  image = models.ImageField(upload_to=user_directory_path)
  description = models.TextField(null=True,blank=True)
  address = models.CharField(max_length = 100)
  contact = models.CharField(max_length = 100)
  date = models.DateTimeField(auto_now_add = True,null = True,blank = True)
  user  = models.ForeignKey(User,on_delete = models.SET_NULL,null=True)
  

  class Meta:
    verbose_name_plural = "Vendors"

  def vendor_image(self):
    return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))
  
  def __str__(self):
    return self.title
  



class Products(models.Model):
  product_id = ShortUUIDField(unique=True,length = 10,max_length = 30,prefix = "product",alphabet="abcdefgh12345")
  title = models.CharField(max_length = 100)
  image = models.ImageField(upload_to=user_directory_path)
  description = models.TextField(null=True,blank=True)
  vendor  = models.ForeignKey(Vendor,on_delete = models.SET_NULL,null=True,related_name = "products")
  price = models.DecimalField(max_digits=10,decimal_places =2)

  user  = models.ForeignKey(User,on_delete = models.SET_NULL,null=True)
  category  = models.ForeignKey(Category,on_delete = models.SET_NULL,null=True) 


  product_status = models.CharField(choices = STATUS,max_length=10,default="in_review")

  status = models.BooleanField(default=True)
  in_stock = models.BooleanField(default = True)
  featured = models.BooleanField(default = False)

  sku = ShortUUIDField(unique=True,length = 4,max_length = 10,prefix = "sku",alphabet="1234567890")

  date = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(null = True,blank = True)

  class Meta:
    verbose_name_plural = "Products"

  def product_image(self):
    return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))
  
  def __str__(self):
    return self.title
  

class CartOrder(models.Model):
  user = models.ForeignKey(User,on_delete = models.CASCADE)
  price = models.DecimalField(max_digits=10,decimal_places =2)
  paid_status = models.BooleanField(default = False)
  order_date = models.DateTimeField(auto_now_add = True)
  product_status = models.CharField(choices = STATUS_CHOICE,max_length = 30,default="processing")

  class Meta:
    verbose_name_plural = "Cart Order"


class CartOrderItems(models.Model):
  order = models.ForeignKey(CartOrder,on_delete = models.CASCADE)
  product_status = models.CharField(max_length = 200)
  item = models.CharField(max_length = 200)
  image = models.CharField(max_length = 200)
  quantity = models.IntegerField()
  price = models.DecimalField(max_digits=10,decimal_places =2)
  total = models.DecimalField(max_digits=10,decimal_places =2)
  invoice_number = models.CharField(max_length = 100)
  class Meta:
    verbose_name_plural = "Cart Order Items"

  def order_img(self):
    return mark_safe('<img src = "/media/%s" width = "50" height = "50 "/>' %(self.image))
  


class Address(models.Model):
  user  = models.ForeignKey(User,on_delete = models.SET_NULL,null=True)
  address = models.CharField(max_length = 100,null = True)
  status = models.BooleanField(default = False)


  class Meta:
    verbose_name_plural = "Address"