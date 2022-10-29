from django import forms
#TODO: figure out how to take in multiple countries as input
class InputParameters(forms.Form):
    startYear = forms.IntegerField()
    endYear = forms.IntegerField()
    inputCountry = forms.CharField()
