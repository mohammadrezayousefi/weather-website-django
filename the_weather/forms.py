from django.forms import  ModelForm , TextInput
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import City
class CityForm(ModelForm):
    help_texts = {
            'name': _('s')
        }
    class Meta:
        model = City
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={'placeholder' : 'مثال : Tehran','class': 'input' }),
        }