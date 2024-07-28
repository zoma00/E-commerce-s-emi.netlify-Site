from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)  # For nested categories

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')  # For storing product images

class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming you'll use Django's built-in authentication
    order_date = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(Product, through='OrderItem')  # For order items

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Store the product price at the time of order


