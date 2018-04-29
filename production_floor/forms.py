from django import forms
from . import models
from django.utils.translation import gettext_lazy as _


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = "__all__"
        widgets = {

        }