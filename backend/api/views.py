from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from product.models import Product
from product.serializers import ProductSerializer

import json 
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
"""

@api_view(["GET"])
def api_home(request,*args,**kwargs):
  instance=Product.objects.all().order_by("?").first()
  data={}
  if instance:
    data=ProductSerializer(instance).data
  return Response(data)
"""


@api_view(["POST,PUT"])
def api_home(request,*args,**kwargs):
  data=request.data
  serializer=ProductSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    print(serializer.data)
    return Response(serializer.data)
  return Response({"error":"invalid data"})
