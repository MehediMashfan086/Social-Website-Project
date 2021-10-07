from django import forms

class looginforms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
