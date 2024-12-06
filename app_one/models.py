from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def expensive(self):
        return self.filter(price__gte=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    objects = ProductManager()

    def __str__(self):
        return self.name