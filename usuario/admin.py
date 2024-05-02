from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    pass
