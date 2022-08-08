from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class Phone_Admin(admin.ModelAdmin):
    list_display = ('name', 'price', 'slug')
    prepopulated_fields = {"slug": ("name",)}
