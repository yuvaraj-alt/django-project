from django.shortcuts import render,redirect
from .models import BookModel
from .forms import BookForm
# Create your views here.

def bookDetails(request):
    data = BookModel.objects.all()
    return render(request, "bookApp/booksDetail.html",{"data":data})

def AddBook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/bookApp/booksData/")
        else:
            return "<h1> Something went wrong </h1>"
    form = BookForm
    return render(request, "bookApp/addBook.html",{"form":form})

def DeleteBook(request,id):
    data = BookModel.objects.get(id=id)
    data.delete()
    return redirect("books")
