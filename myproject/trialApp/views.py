from django.shortcuts import render
from .models import ProductModel
from rest_framework import generics
from .serializers import ProductSerializer
from .pagination import MyNewPagination,MyNewLimitPagination


class ProductView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    # pagination_class = MyNewPagination

class ProductApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    # pagination_class = MyNewLimitPagination
