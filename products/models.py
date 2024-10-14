from django.db import models

#Модель категории
class ProductCategory(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)

#Модель продукта
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=15)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
