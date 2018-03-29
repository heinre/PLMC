from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def index(request):
    return render(request,'base.html')


def login_view(request):
    if request.method == 'POST':
        print(request.POST)
      #  if AuthenticationForm(data=request.POST).is_valid():
       #     HttpResponse('yes')
        #else:
        return render(request,'login.html', {'form': AuthenticationForm(), 'invalid': True})
    else:
        return render(request,'login.html', {'form': AuthenticationForm()})