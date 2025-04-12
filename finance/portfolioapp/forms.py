"""
from django import forms
from .models import *

class MemPaymentForm(forms.ModelForm):
    class meta:
        model= TransactionlogModel
        fields='__all__'
"""   
    
