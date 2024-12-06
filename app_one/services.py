from .models import Product

def get_expensive_products():
    return Product.objects.expensive()