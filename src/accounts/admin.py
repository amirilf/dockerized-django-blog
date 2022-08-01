from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm,CustomUserCreationForm

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    model        = User
    add_form     = CustomUserCreationForm
    form         = CustomUserChangeForm
    list_display = ['email','username']

admin.site.register(User,CustomUserAdmin)