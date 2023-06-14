from  django import forms
from .models import Registrationform

class RegistrationModel(forms.ModelForm):
    class Meta:
        model =Registrationform
        fields ='__all__'