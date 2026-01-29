from django.shortcuts import render,redirect
from .forms import EventForm
from .models import EventModel

# Create your views here.
def eventView(request):
    data = EventModel.objects.all()
    return render(request,"eventApp/eventDetails.html",{"data":data})

def eventAdd(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("event")
        else:
            return "<h1> Something went wrong </h1>"
    form = EventForm
    return render(request,"eventApp/addEvent.html",{"form":form})

def eventUPdte(request,id):
    data = EventModel.objects.get(id=id)
    if request.method == "POST":
        form = EventForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("event")
        else:
            return "<h1> Something went wrong </h1>"
    form = EventForm
    return render(request,"eventApp/addEvent.html",{"form":form})

def eventDelete(request,id):
    data = EventModel.objects.get(id=id)
    data.delete()
    return redirect("event")