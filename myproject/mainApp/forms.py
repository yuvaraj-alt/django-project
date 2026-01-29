from django import forms

class SampleForm(forms.Form):
    passengerName = forms.CharField(max_length=100)
    classType = forms.CharField
    IdProof = forms.CharField(max_length=100)
    startStation = forms.CharField(max_length=100)
    destination = forms.CharField(max_length=100)
    Date = forms.DateField(null=True, blank=True)