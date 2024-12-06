from django.db import models

# Create your models here.
class Order(models.Model):
    product = models.ForeignKey('app_one.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.product.name} x {self.quantity}"