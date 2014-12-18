from django.forms import ModelForm
from django import forms
from web.models import WebUser

class BuscaRecomendacion(forms.Form):
       
    choices  = forms.ChoiceField(choices=[(u,u) for u in WebUser.objects.all()])
    
    