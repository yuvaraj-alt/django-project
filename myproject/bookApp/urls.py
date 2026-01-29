from django.urls import path
from .import views

urlpatterns = [
   path("booksData/",views.bookDetails,name = "books"),
   path("add/",views.AddBook,name = "addData"),
   path("delete/<int:id>/",views.DeleteBook,name = "deleteData")
]