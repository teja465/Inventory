from django import forms
from stocks.models import *
class mobile_form(forms.ModelForm):
    class Meta:
        model=mobile
        fields='__all__'
        
