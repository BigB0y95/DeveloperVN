from django import forms

class register_form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)