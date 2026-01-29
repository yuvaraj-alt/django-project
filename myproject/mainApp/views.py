from django.shortcuts import render, redirect
import requests

URL = "http://127.0.0.1:8000/api/v1/ticket/"

def getData(request):
    data = requests.get(URL).json()
    return render(request, "mainApp/BookTicket.html", {"data": data})


def deleteData(request, id):
    requests.delete(f"{URL}{id}/")
    return redirect("book")





