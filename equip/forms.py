from django import forms
from .models import Equip

class EquipForm(forms.ModelForm):
    class Meta:
        model = Equip
        fields = ["name", "locate", "ipaddress", "etc"]