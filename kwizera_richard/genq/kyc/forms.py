from django.forms import ModelForm

from .models import *

class RegisterationForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'country',
        ]