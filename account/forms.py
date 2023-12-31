from django import forms
from django.contrib.auth import get_user_model, authenticate

user = get_user_model()

class LoginForms(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control", 'type': "text", 'id': "fname", 'placeholder': "login"}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': "form-control", 'type': "password", 'id': "fpas", 'placeholder': "password"}))

    def clean(self):
        username = self.cleaned_data.get('username',)
        password = self.cleaned_data.get('password',)
        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('Невірний логін або пароль!')
            return super().clean()



class RgistrationForms(forms.ModelForm):

    class Meta:
        model = user
        fields = ('username', )

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control", 'type': "text", 'id': "fname", 'placeholder': "login"}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': "form-control", 'type': "text", 'id': "fpas", 'placeholder': "password"}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': "form-control", 'type': "password", 'id': "fpas", 'placeholder': "password2"}))


    def clean_password2(self):
        if self.cleaned_data['password'] == self.cleaned_data['password2']:
            return self.cleaned_data['password2']
        raise forms.ValidationError('Паролі не співпадають!')