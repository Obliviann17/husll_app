from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from .models import Category, Product

def index(request):
    posts = Product.objects.all().order_by('name')[:21]
    return render(request, 'main/index.html', {'posts': posts})

def about(request):
    return render(request, 'main/about_us.html')

def categories(request):
    return render(request, 'main/categories.html')

def category_product(request):
    return render(request, 'main/category_product.html')

def delivery(request):
    return render(request, 'main/delivery.html')

def bookmarks(request):
    return render(request, 'main/bookmarks.html')

def product_page(request):
    return render(request, 'main/product_page.html')

def registration(request):
    return render(request, 'main/register.html')

def error_404(request, exception):
    return render(request, 'main/404.html')


