from django import forms
from . import models
from django.utils.translation import gettext_lazy as _


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = "__all__"
        labels = {'name': _("שם"), 'amount': _("כמות"), 'processes': _("תהליכים")}
        widgets = {
            'processes': forms.Textarea(attrs={'rows': 4, 'cols': 20})
        }