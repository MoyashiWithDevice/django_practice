from django import forms
from .models import Equip

class EquipForm(forms.ModelForm):
    class Meta:
        model = Equip
        fields = ["user", "name", "locate", "ipaddress", "etc"]