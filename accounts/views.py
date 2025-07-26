from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


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
    elif request.method == "POST" and request.user.is_authenticated:
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
    pass
    