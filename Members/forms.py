from django import forms

class register_form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
class login_form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)