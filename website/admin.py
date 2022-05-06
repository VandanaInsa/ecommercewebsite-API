from django.contrib import admin

# Register your models here.
from . models import product
@admin.register(product)
class productAdmin(admin.ModelAdmin):
   list_display=['id','name','category_name','description','buy_price','sell_price','quantity']


   #superuser is  anjali paasword is anjali