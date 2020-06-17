from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombres'
            }
        )
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Apellidos'
            }
        )
    )
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Correo electrónico'
            }
        )
    )

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    confirm_password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmar contraseña'
            }
        )
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'confirm_password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        email_exists = (User.objects.filter(email=cleaned_data.get('email')).count() > 0)
        if email_exists:
            self.add_error('email', 'Usuario ya existe')