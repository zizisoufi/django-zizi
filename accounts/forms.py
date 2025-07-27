from django import forms
from django.contrib.auth.forms import  UserCreationForm
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, max_length=15)
     
    
class SignupForm(UserCreationForm):
    email = forms.EmailField()
    

class ChangePasswordForm(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput, max_length=15)
    password = forms.CharField(widget=forms.PasswordInput, max_length=15)
    confirm = forms.CharField(widget=forms.PasswordInput, max_length=15)
    