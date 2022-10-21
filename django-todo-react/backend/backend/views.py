from django.http import HttpResponse
from django.shortcuts import render
from . import Launchpad
# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello Django!</h1>')
    # context['graph'] = TreeLossChart()
    # return render(request, 'x/dashboard.html', context)

def about(request):
    return HttpResponse('about page')