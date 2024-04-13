from typing import Any
from django import forms
from apps.users.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "type":"password", "placeholder":"password..."
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "type":"password", "placeholder":"password(Choice)..."
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "type":"email", "placeholder":"your email"
    }))
 
    def save(self, commit = True):
        user = super().save(commit)
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 == password2:
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError("Your password choice is not match !")
        
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2", "avatar", "email")

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text", "placeholder":"Your username..."
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text", "placeholder":"Your username..."
    }))
    