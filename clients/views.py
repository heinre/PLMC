from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.messages import error
from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()


def index(request):
    return render(request, 'base.html')


def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homepage')
        else:
            error(request, 'Invalid Username/Password')
            if 'next' in request.POST:
                return redirect('/login/?next=%s' % request.POST.get('next'))
            return redirect('login')
    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('homepage')
