from django import forms

from .models import Ticket

class TicketForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"popup_input", 'placeholder': 'Имя', 'required': 'required'}), label='')
    service = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"popup_input", 'placeholder': 'Услуга', 'required': 'required'}), label='')
    tel_number = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"popup_input", 'placeholder': 'Номер телефона','type': 'tel', 'required': 'required'}), label='')
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"popup_input", 'placeholder': 'Email *'}), label='', required=False)

    class Meta:
        model = Ticket
        fields = ['name', 'service', 'tel_number', 'email']
        

        
        #widgets = {
        #        'name': forms.TextInput(
        #            attrs={'class': 'popup_input', 'placeholder': 'First Name', 'required': 'required'}),
        #        'service': forms.TextInput(
        #            attrs={'class': 'popup_input', 'placeholder': 'Last Name', 'required': 'required'}),
        #        'tel_number': forms.TextInput(
        #            attrs={'class': 'popup_input', 'placeholder': 'Trading Acc No: (For Login)', 'required': 'required'}),
        #        'email': forms.TextInput(
        #            attrs={'class': 'popup_input', 'placeholder': 'Password', 'lable': ''}),
        #    }
        