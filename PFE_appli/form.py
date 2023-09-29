from django import forms
from .models import Village 
from .models import Foret, Foret_sacree

class VillageForm(forms.ModelForm):
    class Meta:
        model = Village
        fields = ("village","nombre_de_forêts")


class ForetForm(forms.ModelForm):
    class Meta:
        model = Foret
        fields = ("village","nom_du_propriétaire","superficie_en_hectare","nature_de_la_forêt")

class Foret_Sacree_Form(forms.ModelForm):
    class Meta:
        model = Foret_sacree
        fields = ("village","nom_du_responsable","superficie_en_hectare")
        

