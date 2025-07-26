from django.urls import path
from .views import login_view, signup_view, logout_view, change_password


app_name = "accounts"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("signug/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("change-password/", change_password, name="change-pass"),
]
