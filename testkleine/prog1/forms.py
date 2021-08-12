from django import forms
from django.forms import ModelForm
from prog1.models import Artikel

class Person(forms.Form):
        first_name = forms.CharField(label='Vorname',  max_length=100)
        last_name = forms.CharField(label='Nachname', max_length=100)

class ArtikelForm(ModelForm):
        class Meta:
                model=Artikel
                fields=["matnr", "maktx_1", "maktx_2", "lifnr", "aritkelbild"]