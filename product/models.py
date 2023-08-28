from django.db import models
from django.contrib.auth import User 
from django.utils import timezone
# Create your models here.
FLAG_TYPES =[
    ('Sale','Sale'),
    ('New','New'),
    ('Feature','Feature'),
]




class Product(models.Model):
    name = models.CharField(max_length=120)
    flag = models.CharField(max_length=10,choices=FLAG_TYPES)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    sku = models.CharField(max_length=12)
    subtitle = models.CharField(max_length=300)
    description = models.TextField(max_length=40000)
    quantity = models.IntegerField()
    brand = models.ForeignKey('Brand',related_name='produc_brand', on_delete=models.SET_NULL, null=True)



class ProductImages(models.Model):
    pass




class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')
    
    def __str__(self):
        return self.name
    

class Review(models.Model):
    user = models.ForeignKey(User, related_name='review_author', on_delete=models.SET_NULL , null=True)
    product = models.ForeignKey(Product, related_name='review_product', on_delete=models.CASCADE)
    rate = models.IntegerField()
    review = models.CharField(max_length=300)
    created_at = models.DateField(default=timezone.now)





