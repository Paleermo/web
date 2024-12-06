from django.shortcuts import render
from .models import Order

# Create your views here.
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'app_two/order_list.html', {'orders': orders})