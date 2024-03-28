from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import Vendor
from userauths.models import User,Profile

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"USER NAME","class":"input"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"EMAIL","class":"input"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"PASSWORD","class":"input"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"CONFIRM PASSWORD","class":"input"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','is_staff']



class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"FULL NAME","class":"support-form-input"}))
    image = forms.CharField(widget=forms.FileInput(attrs={"class": "support-form-input"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"MOBILE","class":"support-form-input"}))


    class Meta:
        model = Profile
        fields = ["full_name","image","phone"]


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['title', 'image', 'description', 'address', 'contact']