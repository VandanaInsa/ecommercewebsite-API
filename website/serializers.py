from rest_framework import serializers
from .models import  product
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields=['id','name','category_name','description','buy_price','sell_price','quantity']