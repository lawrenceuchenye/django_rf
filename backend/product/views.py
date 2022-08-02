
from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product

from rest_framework import generics,mixins
# Create your views here.

class ProductMixinView(mixins.ListModelMixin,generics.GenericAPIView):
   queryset=Product.objects.all()
   serializer_class=ProductSerializer

   def get(self,request,*args,**kwargs):
     return self.list(request,*args,**kwargs)


class  ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class  ProductUpdateAPIView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_update(self,serializer):
      serializer.save()

class  ProductCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self,serializer):
       print(serializer.validated_data)
       serializer.save()


class  ProductDeleteAPIView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_destroy(self,instance):
       super().perform_destroy(instance)
