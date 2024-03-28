from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.conf import settings
from userauths.models import User
# Create your views here.

def register_view(request):
  if request.method == "POST":
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
      new_user = form.save()
      username = form.cleaned_data.get("username")
      messages.success(request,"Your account has been created successfully.")
      new_user = authenticate(username = form.cleaned_data.get("username"),password = form.cleaned_data.get("password1"))
      login(request,new_user)
      return redirect("core:index")
  else:
    print("can not register")
    form = UserRegisterForm()
  context = {
    'form':form
  }
  return render(request,"userauths/signup.html",context)




def login_view(request):
  if request.user.is_authenticated:
    messages.warning(request, "Hey ! You are already logged in.")
    return redirect("core:index")
  
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      messages.success(request, "Login successful")
      return redirect("core:index")
    else:
      messages.warning(request, "Invalid username or password.")
    
  return render(request, "userauths/login.html")


def logout_view(request):
  logout(request)
  messages.success(request,"You have logged out successfully.")
  return redirect("userauths:login")

def redirect_view(request):
  if not request.user.is_authenticated:
    messages.warning(request,"You need to login to use this functionality.")
    return redirect('userauths:login')
  else:
    return render(request,'userauths/account.html')
  


