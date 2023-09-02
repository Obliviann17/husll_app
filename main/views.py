from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from django.contrib import messages

from .models import Category, Product

def index(request):
    user = request.user
    posts = Product.objects.all().order_by('name')[:21]
    cats = Category.objects.all()

    context = {
            'posts': posts,
            'cats': cats,
            'cat_selected': 0,
            'user': user
    }

    return render(request, 'main/index.html', context=context)

def about(request):
    return render(request, 'main/about_us.html')

def user_profile(request):
    return render(request, 'main/user_profile.html')

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

def wishlist(request):
    return render(request, 'main/wishlist.html')

def product_page(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    recommended_products = Product.objects.filter(cat=product.cat).exclude(id=product_id)[:4]
    context = {
        'product': product,
        'recommended_products': recommended_products,
    }
    return render(request, 'main/product_page.html', context=context)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Ви ввійшли як {user}.')
                return redirect('home')
            else:
                messages.error(request, 'Невірний email або пароль.')
        else:
            messages.error(request, 'Невірний email або пароль.')
    form = AuthenticationForm()
    return render(request=request, template_name='main/login.html', context={'login_form': form})

def logout_request(request):
    logout(request)
    messages.info(request, "Ви успішно вийшли з акаунта!")
    return redirect('home')

def registration(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Ви успішно зареєструвались.')
            return redirect('home')
        else:
            messages.error(request, "Неуспішна реєстрація. Невірна інформація.")
    else:
        form = NewUserForm()
    return render(request=request, template_name='main/register.html', context={'register_form': form})

def error_404(request, exception):
    return render(request, 'main/404.html')

# Function for searching the site
def search(request):
    query = request.GET.get('q')
    if query:
        # This option to search all databases

        # products = Product.objects.filter(name__icontains=query)

        # This option for searching the SQLite database
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(name__icontains=query.capitalize())
        )
    else:
        products = Product.objects.none()

    context = {
        'Products': products,
        'q': query
    }
    return render(request, 'main/search.html', context=context)