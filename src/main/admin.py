from django.contrib import admin
from .models import Modal
# Register your models here.

@admin.register(Modal)
class ProjectsAdmin(admin.ModelAdmin):
    list_display: Modal._meta.get_fields()
