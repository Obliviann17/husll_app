from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'main_price', 'discount_price', 'description', 'photo', 'available')
    list_display_links = ('id', 'name')

admin.site.register(Product, ProductAdmin)
