from django import forms
from .models import Usermodel


class Userform(forms.ModelForm):
    class Meta:
        model = Usermodel
        fields = ["name" , "email" , "age"]