from django import forms

INTEGER_CHOICES= [tuple([x, x]) for x in range(2001, 2022)]


class InputForm(forms.Form):

   startYear = forms.IntegerField(label = "Start Year ", widget = forms.Select(choices = INTEGER_CHOICES))

   endYear = forms.IntegerField(label = "End Year  ", widget = forms.Select(choices = INTEGER_CHOICES))

   countries = forms.CharField(max_length=100)