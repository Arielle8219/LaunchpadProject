from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Hello Django!</h1>')
    return render(request, 'homepage.html')

def about(request):
    return HttpResponse('about page')