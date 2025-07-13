from django.urls import path
from .views import services,service_detail, service_null

app_name = "services"

urlpatterns = [
    path("" , services, name = "services"),
    path("detail/<int:id>" , service_detail, name="service_detail"),
    path("detail/" , service_null, name="service_null"),
]
