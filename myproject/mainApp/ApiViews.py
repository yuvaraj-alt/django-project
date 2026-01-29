from .models import  TicketBooking
from .serializers import ticketSerializer
from rest_framework import generics

class ticketApi(generics.ListCreateAPIView):
    queryset = TicketBooking.objects.all()
    serializer_class = ticketSerializer

class ticketApiCon(generics.RetrieveUpdateDestroyAPIView):
    queryset = TicketBooking.objects.all()
    serializer_class = ticketSerializer
    lookup_field = "pk"