from django import forms
from .models import PartnerRequest,ContactMessage

class PartnerRequestForm(forms.ModelForm):
    class Meta:
        model = PartnerRequest
        fields = ['name', 'email','phone', 'message']


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class DonationForm(forms.Form):
    donor_name = forms.CharField(max_length=100)
    donor_email = forms.EmailField()
    amount = forms.DecimalField(max_digits=10, decimal_places=2)        