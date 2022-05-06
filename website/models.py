from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=50)
    category_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    buy_price=models.IntegerField()
    sell_price=models.IntegerField()
    quantity=models.IntegerField()