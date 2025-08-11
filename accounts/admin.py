from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomeUser(UserAdmin):
    list_display = ["username", "email", "id_code"]

admin.site.register(User, CustomeUser)
