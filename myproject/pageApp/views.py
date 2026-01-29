from django.shortcuts import render
from .models import PageModel
from .serializers import PageSerializer
from rest_framework import generics
from .pagination import PageCustomPagination,PageLimitPagination
# Create your views here.

class PageView(generics.ListCreateAPIView):
    queryset = PageModel.objects.all()
    serializer_class = PageSerializer
    pagination_class = PageCustomPagination

class PageNumView(generics.ListCreateAPIView):
    queryset = PageModel.objects.all()
    serializer_class = PageSerializer
    pagination_class = PageLimitPagination



