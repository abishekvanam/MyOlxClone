from django import forms

class SignUpForm(forms.Form):
    first_name=forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter first name'})
    )
    last_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter first name'})
    )
    email=forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter first name'})
    )
    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter first name'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter first name'})
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter username'})

    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter password'})
    )


