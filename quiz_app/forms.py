from django import forms
from .models import Quiz_Registration_Form

class My_Quiz(forms.ModelForm):
    class Meta:
        model = Quiz_Registration_Form
        fields = ["Name","Contact","Mail"]