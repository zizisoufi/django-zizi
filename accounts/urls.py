from django.urls import path
from .views import login_view, signup_view, logout_view, change_password,password_reset ,password_reset_confirm


app_name = "accounts"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("signug/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("change-password/", change_password, name="change-pass"),
    path("password_reset/", password_reset, name="password_reset"),
    path("reset-password-confirm/<str:uid>/<str:token>",password_reset_confirm, name="confirm") 
]
