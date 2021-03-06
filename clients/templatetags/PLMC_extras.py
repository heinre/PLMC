from django import template
from django.utils import timezone
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='modulo')
def modulo(num, val):
    return num % val


@register.filter(name='timestamp')
def timestamp(stamp):
    return timezone.datetime.fromtimestamp(stamp)

@register.filter(name='serialNum')
def serialNum(number):
    return str(number).zfill(6)
