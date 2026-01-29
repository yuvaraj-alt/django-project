from .models import AppointModel
from django import forms

class AppointForm(forms.ModelForm):
    class Meta:
        model = AppointModel
        fields = "__all__"