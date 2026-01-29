from .models import StockModel
from django import forms

class StockForm(forms.ModelForm):
    class Meta:
        model = StockModel
        fields = "__all__"