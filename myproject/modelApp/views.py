from django.shortcuts import render
from .models import Players

def playersTable(request):
    players = Players.objects.all()
    return render(request, "modelApp/players.html", {
        "players": players
    })