from django.urls import path
from userauths import views

app_name = 'userauths'

urlpatterns = [
  path("sign-up/",views.register_view,name="sign-up"),
  path("login/",views.login_view,name="login"),
  path("signout/",views.logout_view,name="sign-out"),
  path('account/',views.redirect_view,name="account"),
 
]