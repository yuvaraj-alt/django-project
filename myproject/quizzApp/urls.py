from django.urls import path
from .import views

urlpatterns = [
  path("Question/",views.QuestionPage, name = "Ques"),
  path("Result/", views.ResultPage,name = "Res"),
]