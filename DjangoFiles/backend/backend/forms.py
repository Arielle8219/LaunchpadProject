from django import forms

startList = [tuple([x, x]) for x in range(2001, 2021)]
endList = [tuple([x, x]) for x in range(2002, 2022)]


class InputForm(forms.Form):

   startYear = forms.IntegerField(label = "Start Year ", widget = forms.Select(choices = startList))

   endYear = forms.IntegerField(label = "End Year  ", widget = forms.Select(choices = endList))

   countries = forms.CharField(max_length=100)