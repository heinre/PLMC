from django import forms
from . import models
from django.utils.translation import gettext_lazy as _


class StationNew(forms.ModelForm):

    class Meta:
        model = models.Station
        fields = "__all__"
        labels = {'type': _("סוג")}
        widgets = {
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = "__all__"
        labels = {'name': _("שם"), 'amount': _("כמות"), 'processes': _("תהליכים"),
                  'done_processes': _("תהליכים שהסתיימו"), 'schema': _("מספר שרטוט"), 'edition': _("מהדורה/גרסה"),
                  'CN': _("מק\"ט"), 'coc_needed': _("C.O.C")}
        widgets = {
            'processes': forms.TextInput(),
        }
