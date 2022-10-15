from django import forms

class InputParameters(forms.Form):
    startYear = forms.IntegerField()
    endYear = forms.IntegerField()
    inputCountry = forms.CharField()

   