from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class RegistraUsuarioForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, label='Primeiro nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, label='Último nome', widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = Usuario
        fields =['username', 'email', 'first_name', 'last_name']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
          'class': 'form-control',
        })
        self.fields['username'].label = 'Nome de usuário'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'