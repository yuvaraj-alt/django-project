from django.urls import path
from .import views


urlpatterns = [
    path("product/",views.ProductView.as_view(),name = "product"),
    path("product/<int:pk>/",views.ProductApiView.as_view(),name = "productDetail")
]