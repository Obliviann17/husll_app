from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'main_price', 'discount_price', 'description', 'photo', 'available']
    list_filter = ['available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)