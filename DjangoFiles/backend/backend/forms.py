from django import forms

class InputForm(forms.Form):

   startYear = forms.IntegerField()

   endYear = forms.IntegerField()

   countries = forms.CharField(max_length=100)