from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HTTPResponse('<h1>Hello Django!</h1>')