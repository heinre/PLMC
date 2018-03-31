from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from re import compile
from django.core.urlresolvers import reverse
from django.utils.deprecation import MiddlewareMixin
from django.contrib.messages import error, info
EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

MANAGER_URLS = []
if hasattr(settings, 'MANAGER_ONLY_URLS'):
    MANAGER_URLS += [compile(expr) for expr in settings.MANAGER_ONLY_URLS]


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        next = request.path_info
        if not request.user.is_authenticated:
            if not any(m.match(path) for m in EXEMPT_URLS):
                return redirect('/login/?next=%s' % next)
        else:
            if not request.user.groups.filter(name='Manager').exists():
                if not any(m.match(path) for m in EXEMPT_URLS) and any(m.match(path) for m in MANAGER_URLS):
                    info(request, 'Permission Denied, You Need Admin Permissions For Access')
                    return redirect('/login/?next=%s' % next)

