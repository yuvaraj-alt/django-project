from django.urls import path
from .import views

urlpatterns = [
  path("stock/",views.StockView,name = "stk"),
  path("stackAdd/",views.StockAddView,name = "stakAdd"),
  path("deleteStock/<int:id>/",views.stockdelete,name = "dltStk"),
  path("uppDateStock/<int:id>/",views.uptStock,name = "upStock")
]