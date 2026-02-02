from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AppointModel
from .forms import AppointForm
# Create your views here.

def appointView(request):
     data = AppointModel.objects.all()
     return render(request, "appointmentApp/appointDetails.html",{"data":data})

def addAppoint(request):
     if request.method == "POST":
          form = AppointForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect("appointMent")
          else:
               return "<h1> Something went wrong </h1>"
     form = AppointForm
     return render(request, "appointmentApp/addDetails.html",{"form":form})

def UpdateView(request,id):
    data = AppointModel.objects.get(id=id)
    if request.method == "POST":
        form = AppointForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("appointMent")
        else:
             return HttpResponse("<h1>Something went wrong</h1>")
    form = AppointForm()
    return render(request, "appointmentApp/addDetails.html", {"form": form})

def deleteView(request, id):
    data = AppointModel.objects.get(id=id)
    data.delete()
    return redirect("appointMent")

