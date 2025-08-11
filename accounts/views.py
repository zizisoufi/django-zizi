from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm, ChangePasswordForm, PasswordReset 
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import password_validation, update_session_auth_hash  
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from .models import User
# Create your views here.


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        context = {
            'form' : form
        }
        return render(request, "accounts/login.html",context=context)
    else :
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else :
                messages.add_message(request, messages.ERROR, "username or password is not valid")
                return redirect(request.path_info)
        else:
            messages.add_message(request, messages.ERROR, "inputdata is not valid")
            return redirect(request.path_info)


def signup_view(request):
    if request.method == "GET" :
         form = SignupForm()
         context = {
            'form' : form
         }
         return render(request, "accounts/signup.html",context=context)
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "registration complete successfully")
            return redirect("accounts:login")
        else:
             messages.add_message(request, messages.ERROR, "registration data is not valid")
             return redirect(request.path_info)
         
         
         
         
@login_required  
def logout_view(request): 
    logout(request)
    return redirect("/")


@login_required
def change_password(request):
    if request.method == "GET" :
        form = ChangePasswordForm()
        context = {
            'form' : form
        }
        return render(request, "accounts/change_password.html", context=context)
    elif request.method == "POST":
        form =ChangePasswordForm(request.POST)
        if form.is_valid():
            old_pass = form.cleaned_data["old_pass"]
            password = form.cleaned_data["password"]
            confirm = form.cleaned_data["confirm"]
            if password == confirm and password != old_pass:
                user = request.user
                if user.check_password(old_pass):
                    try:
                        password_validation.validate_password(password, user=user)
                        user.set_password(password)
                        user.save()
                        update_session_auth_hash(request, user)
                        messages.add_message(request, messages.SUCCESS, "change password complete successfully")
                        return redirect(request.path_info)
                    except:
                        messages.add_message(request, messages.ERROR, "new password str is not valid")
                        return redirect(request.path_info)
                else:
                    messages.add_message(request, messages.ERROR, "old pass is no valid")
                    return redirect(request.path_info)
            else:
                  messages.add_message(request, messages.ERROR, "pass1 and pass2 not same")
                  return redirect(request.path_info)
              
              
              
def password_reset(request):
    if request.method == "GET":
        form = PasswordReset()
        context = {
            'form' : form 
        }
        return render(request, "accounts/reset_password.html", context=context)
    elif request.method == 'POST':
        form = PasswordReset(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
                uid = urlsafe_base64_encode(force_bytes(user.id))
                token_generator = PasswordReetTokenGenerator()
                token = token_generator.make_token(user)
                url = f"http://127.0.0.1:8000/accounts/reset-password-confirm/{uid}/{token}"
                send_mail(
                    "reset password",
                    url,
                    "admin@example.com",
                    [user.email],
                    fail_silently=True,
                )
                return render(request, "accounts/password_reset_done.html")
                
                  
            except User.DoesNotExist:
                messages.error(request, "user not found")
                return redirect("accounts.signup") 
                
            
        
                    
def password_reset_confirm(request, uid, token):
    token_generator = PasswordResetTokenGenerator()
    try :
        uid = urlsafe_base64_decode(uid).decode()
        user = User.objects.get(id=uid)
    except:
        user = None
    if user and token_generator.check_token(user, token):
        if request.method == "GET" :
            form = ResetPasswordForm()
            context = {
                'form' : form
            }
            return render(request, "accounts/reset_password_confirm.html", context=context)
        else:
            form = ResetPasswordForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password']
                confirm = form.cleaned_data['confirm']
                if password == confirm :
                    try:
                        password_validation.validate_password(password)
                        user.set_password(password)
                        user.save()
                        return render(request, "accounts/reset_password_complete.html")
                    except:
                        messages.add_message(request, messages.ERROR, "new pass not valid")
                        return redirect(request.path_info)
                else:
                    messages.add_message(request, messages.ERROR, "pass and conf must be same")
                    return redirect(request.path_info)
            else:
                messages.add_message(request, messages.ERROR, "input data is not valid")
                return redirect(request.path_info)
            
        
     
    
    
       
                      
                       
        
    
