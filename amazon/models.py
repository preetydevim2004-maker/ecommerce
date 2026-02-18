from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (('pending', 'pending'), ('shipped', 'shipped'), ('delivered', 'delivered'))
    status = models.CharField(max_length=15, choices=STATUS, default='Pending')

    PAYMENT = (('pending', 'pending'), ('paid', 'paid'), ('failed', 'failed'))
    payment = models.CharField(max_length=20, choices=PAYMENT, default='Pending')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    address = models.TextField(default='Not Provided')
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"Order {self.id}"




class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name
