from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from account.forms import UserLoginForm
from .models import Category, Product



def product_all(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})

def Index (request):
    context = {'form':UserLoginForm()}
    return render(request, 'index.html',context)