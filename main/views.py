from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from .models import Category, Product

def index(request):
    posts = Product.objects.all().order_by('name')[:21]
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'cat_selected': 0,
    }

    return render(request, 'main/index.html', context=context)

def about(request):
    return render(request, 'main/about_us.html')

def categories(request):
    cats = Category.objects.all()
    context = {
        'cats': cats,
    }

    return render(request, 'main/categories.html', context=context)

def category_product(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(cat=category)

    context = {
        'category': category,
        'products': products,
        'px': category_id,
    }

    return render(request, 'main/category_product.html', context=context)

def delivery(request):
    return render(request, 'main/delivery.html')

def bookmarks(request):
    return render(request, 'main/bookmarks.html')

def product_page(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    recommended_products = Product.objects.filter(cat=product.cat).exclude(id=product_id)[:4]
    context = {
        'product': product,
        'recommended_products': recommended_products,
    }
    return render(request, 'main/product_page.html', context=context)

def registration(request):
    return render(request, 'main/register.html')

def error_404(request, exception):
    return render(request, 'main/404.html')


