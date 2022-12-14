from cProfile import label
from tabnanny import verbose
from attr import fields
from django.contrib.auth.forms import AuthenticationForm , UsernameField , UserCreationForm 
from django import forms
from django.contrib.auth.models import User
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs) :
        super(UserLoginForm , self).__init__(*args, **kwargs)


    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control form-control-lg' ,
            'placeholder': '',
            'id': 'hi',
        }
))

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='' ,widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}))
    fullname =forms.CharField(label ='' ,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Your Name'}))
    username = UsernameField(label='' ,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'}))
    password1= forms.CharField(label ='' ,widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'password'}))
    password2=forms.CharField(label='',widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Repeat your password'}))
    
    class Meta :
        model = User
        fields = ["fullname" ,"username", "email"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with that email already exists")
        return email
