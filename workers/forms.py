from django import forms
from . import models
from django.utils.translation import gettext_lazy as _


class WorkerNew(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get("phone")
        email = cleaned_data.get("email")

        if not phone and not email:
            msg = "Must add at least 1 contact measure."
            self.add_error('email', msg)

    class Meta:
        model = models.Worker
        fields = "__all__"
        labels = {'firstName': _("שם פרטי"), 'lastName': _("שם משפחה"), 'address': _("כתובת"), 'email': _('דוא"ל'),
                  'phone': _("טלפון"), 'skills': _("כישורים")}
        widgets = {
            'skills': forms.TextInput,
        }
