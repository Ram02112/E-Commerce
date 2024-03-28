from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  email = models.EmailField(unique = True)
  username = models.CharField(max_length = 100,unique = True)
  bio = models.CharField(max_length = 100)
  

  REQUIRED_FIELDS = ['email']

  def __str__(self):
    return self.username


  

class Profile(models.Model):
  user = models.ForeignKey(User,on_delete = models.CASCADE)
  full_name = models.CharField(max_length=200)
  bio = models.CharField(max_length=200,null=True,blank = True)
  image = models.ImageField(upload_to="image")
  phone = models.CharField(max_length = 200)
  verified = models.BooleanField(default=False)

  def __str__(self):
    return self.full_name
  

class ContactUs(models.Model):
  user_name = models.CharField(max_length = 200)
  email = models.EmailField(max_length = 200)
  phone = models.CharField(max_length = 200)
  subject = models.CharField(max_length = 200)
  message = models.TextField()

  class Meta:
    verbose_name = "Contact Us"
    verbose_name_plural = "Contact Us"
  def __str__(self):
    return self.user_name