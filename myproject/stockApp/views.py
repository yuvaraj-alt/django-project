from django.shortcuts import render,redirect,get_object_or_404
from .models import StockModel
from .forms import StockForm
# Create your views here.

def StockView(request):
    data = StockModel.objects.all()
    return render(request,"stockApp/stockDetails.html",{"data":data})

def StockAddView(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/stockApp/stock")
        else:
            return "<h1> Something went wrong </h1>"
    form = StockForm
    return render(request,"stockApp/addStock.html",{"form":form})

def uptStock(request,id):
    data = StockModel.objects.get(id=id)
    if request.method == "POST":
        form = StockForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("stk")
        else:
            return "<h1> Something went wrong </h1>"
    form = StockForm
    return render(request,"stockApp/addStock.html",{"form":form})

def stockdelete(request,id):
    data = StockModel.objects.get(id=id)
    data.delete()
    return redirect("/stockApp/stock")


