from django import forms
from .models import MedicalImage

class MedicalImageForm(forms.ModelForm):
    class Meta:
        model = MedicalImage
        fields = ['image']  

