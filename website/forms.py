from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(label = "", widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label = "", max_length=100, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label = "", max_length=100, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignupForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].wedget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class = "form-text text-muted><small>Type your username</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].wedget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class = "form-text text-muted><small>I am a helper, but not initialized yet :)</small></span>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].wedget.attrs['placeholder'] = 'Re-type password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class = "form-text text-muted><small>I am a helper, but not initialized yet :)</small></span>'
