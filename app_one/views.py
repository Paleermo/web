from django.shortcuts import render
from .models import Product
from .services import get_expensive_products

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'app_one/product_list.html', {'products': products})

def expensive_products(request):
    products = get_expensive_products()
    return render(request, 'app_one/expensive_products.html', {'products': products})