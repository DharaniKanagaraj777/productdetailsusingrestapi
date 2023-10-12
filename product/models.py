from django.db import models

# Create your models here.
class ProductDetail(models.Model):
    customername=models.CharField(max_length=30)
    productname=models.CharField(max_length=30)
    quantity=models.IntegerField()
    address=models.CharField(max_length=20)
   