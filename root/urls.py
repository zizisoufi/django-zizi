from django.urls import path
from .views import home,contact,about, pricing

app_name = "root"

urlpatterns = [
    path("" , home, name = "home"),
    path("contact", contact, name = "contact"),
    path("about", about, name = "about"),
    path("pricing", pricing, name = "pricing"),
]