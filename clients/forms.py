from django import forms
from . import models
from django.utils.translation import gettext_lazy as _


class ClientNew(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get("contactPhone")
        email = cleaned_data.get("contactEmail")

        if not phone and not email:
            msg = "Must add at least 1 contact measure."
            self.add_error('contactName', msg)

    class Meta:
        model = models.Client
        fields = "__all__"
        labels = {'name': _("שם"), 'address': _("כתובת"), 'contactName': _("שם איש הקשר"), 'contactEmail': _('דוא"ל'),
                  'contactPhone': _("טלפון איש הקשר"), 'remarks': _("הערות")}
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
