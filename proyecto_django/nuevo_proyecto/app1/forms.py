from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from app1.models import PerfilDeUsuario

class UserForm(forms.ModelForm):
    password = forms.CharField(min_length=8,widget=PasswordInput(attrs={'placeholder': 'Ingrese su contraseña','class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Ingrese su nombre de usuario','class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingrese su correo electrónico','class':'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Ingrese su nombre','class':'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ingrese su apellido','class':'form-control'}),
        }
     

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilDeUsuario
        fields = ['edad', 'profesion', 'direccion', 'comuna']
        widgets = {
            'edad': forms.NumberInput(attrs={'placeholder': 'Ingrese su edad','class':'form-control'}),
            'profesion': forms.TextInput(attrs={'placeholder': 'Ingrese su profesión','class':'form-control'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingrese su dirección','class':'form-control'}),
            'comuna': forms.TextInput(attrs={'placeholder': 'Ingrese su comuna','class':'form-control'})  }

class LoginUsuarioForm(forms.Form):
    usuario= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese su username','class':'form-control'}),max_length=50,required=True,label='Nombre de usuario')
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña','class':'form-control'}), max_length=20,label='Password',required=True,error_messages={'required':'La contraseña es obligatoria'})