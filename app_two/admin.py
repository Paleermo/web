from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'date')
    list_filter = ('date',)

admin.site.register(Order, OrderAdmin)