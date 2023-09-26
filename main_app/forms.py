from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'message')

    name = forms.CharField(max_length=100, widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "text", 'id': "fname", 'placeholder': "ім'я"}))

    email = forms.EmailField(widget=forms.TextInput(
            attrs={'type': "email", 'class': "form-control", 'id': "exampleInputEmail1", 'placeholder': "Ваш email"}))

    phone = forms.CharField(max_length=16, widget=forms.TextInput(
            attrs={'type': "subject", 'id': "subject", 'class': "form-control", 'aria-describedby': "phoneHelp",
                   'placeholder': "Ваш телефон"}))

    message = forms.CharField(max_length=1000, required=None, widget=forms.Textarea(
            attrs={' name': "message", 'id': "message", 'cols': "30", 'rows': "7", 'class': "form-control",
                   'placeholder': "Напишіть свої коментарі або запитання тут...", }))