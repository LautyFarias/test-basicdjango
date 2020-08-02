from django import forms
from apps.adopcion.models import Persona, Solicitud


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'e-mail',
            'domicilio': 'Domicilio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'domicilio': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'nro_mascotas',
            'razones',
        ]
        labels = {
            'nro_mascotas': 'Cantidad de Mascotas',
            'razones': 'Razones',
        }
        widgets = {
            'nro_mascotas': forms.TextInput(attrs={'class': 'form-control'}),
            'razones': forms.Textarea(attrs={'class': 'form-control'}),
        }
