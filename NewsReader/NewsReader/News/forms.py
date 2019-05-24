#give generic user class we can use
from django.contrib.auth.models import User
from django import forms
#make a new user form class thats going to tweak it to whatever we want to display om forms
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta: #info about class
        model = User
        fields = ['username','email','password']
