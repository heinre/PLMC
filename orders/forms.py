from django import forms
from . import models
from django.utils.translation import gettext_lazy as _


class OrderNew(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = "__all__"
        labels = {'clientID': _("לקוח"), 'dueDate': _("יעד לסיום"), 'remarks': _("הערות")}
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'processes': forms.Textarea(attrs={'rows': 4, 'cols': 20}),
            'products': forms.Textarea(attrs={'rows': 4, 'cols': 20}),
        }

    '''
    def __init__(self, *args, **kwargs):
        super(OrderNew, self).__init__(*args, **kwargs)
        self.fields['dueDate'].widget = forms.widgets.SplitDateTimeWidget()
        
        self.fields['mytime'].widget = widgets.AdminTimeWidget()
        self.fields['mydatetime'].widget = widgets.AdminSplitDateTime()
        '''