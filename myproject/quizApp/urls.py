from django.urls import path
from .import views

urlpatterns = [
   path("questions/",views.questionPage,name="ques"),
   path("result/", views.resultPage,name = "res"),
]