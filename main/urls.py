from django.template.defaulttags import url

from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('delivery/', views.delivery, name='delivery'),
    path('wishlist/', views.bookmarks, name='bookmarks'),
    path('product/', views.product_page, name='product_page'),
    path('registration/', views.registration, name='registration'),
    path('404/', views.error_404, name='404-error'),
    path('category_product/', views.category_product, name='category_product')
]
