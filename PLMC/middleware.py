from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from re import compile
from django.core.urlresolvers import reverse
from django.utils.deprecation import MiddlewareMixin
from django.contrib.messages import error
EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

MANAGER_URLS = []
if hasattr(settings, 'MANAGER_EXEMPT_URLS'):
    MANAGER_URLS += [compile(expr) for expr in settings.MANAGER_EXEMPT_URLS]


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, 'user')
        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                next = request.path_info
                return redirect('/login/?next=%s' % next)
        if not request.user.groups.filter(name='Manager').exists():
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS) and not any(m.match(path) for m in MANAGER_URLS):
                print('no manager')
                next = request.path_info
                error(request, 'Permission Denied, You Need Admin Permissions For Access')
                return redirect('/login/?next=%s' % next)
