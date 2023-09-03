from django.template.defaulttags import url

from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),
    path('delivery/', views.delivery, name='delivery'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('product/<int:product_id>', views.product_page, name='product_page'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_request, name='login'),
    path('404/', views.error_404, name='404-error'),
    path('category_product/<int:category_id>', views.category_product, name='category_product'),
    path('search/', views.search, name='search'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.logout_request, name='logout'),
    path('change_password', views.change_pass, name='change_password'),
    path('user_data/', views.user_data, name='user_data'),
    path('user_adress/', views.update_address, name='adress'),
]

handler404 = 'main.views.error_404'
