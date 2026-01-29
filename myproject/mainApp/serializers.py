from rest_framework import serializers
from .models import TicketBooking

class ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketBooking
        fields = "__all__"

