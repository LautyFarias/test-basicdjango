from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'e-mail',
        }
