from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('bid_start_date')
    serializer_class = ProductSerializer
# Create your views here.
