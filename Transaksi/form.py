from django import forms
from .models import modelTransaksi

class TransaksiForm(forms.ModelForm):
    """Form definition for Transaksi."""

    class Meta:
        """Meta definition for Transaksiform."""
        model = modelTransaksi
        fields = "__all__"
        widgets = {
        	"jumlah": forms.NumberInput(attrs={'min': 1}),
        	"paket": forms.TextInput(attrs={'type':'hidden'}),
        	"user": forms.TextInput(attrs={'type':'hidden'}),
        }


