from .models import PageModel
from rest_framework import serializers

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageModel
        fields = '__all__'