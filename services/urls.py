from django.urls import path
from .views import services,service_detail, service_null

app_name = "services"

urlpatterns = [
    path("" , services, name = "services"),
    path("category/<str:cat>" , services, name="services_by_cate"),
    path("creator/<str:user>" , services, name="services_by_user"),
    path("detail/<int:id>" , service_detail, name="service_detail"),
    path("detail/" , service_null, name="service_null"),
]
