from django.shortcuts import render

# Create your views here.
from rest_framework.generics import  GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from . models import product
from .serializers import productSerializer

class LCproductAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=product.objects.all()
    serializer_class  =productSerializer

    def get(self,request, *args, **kwargs) :
        return self.list(request, *args, **kwargs)

    def post(self,request,*args,**kwargs) :
        return self.create(request,*args,**kwargs)



class RUDproductAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = product.objects.all()
    serializer_class = productSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve( request, *args, **kwargs )

    def put(self, request, *args, **kwargs):
        return self.update( request, *args, **kwargs )

    def delete(self, request, *args, **kwargs):
        return self.destroy( request, *args, **kwargs )

