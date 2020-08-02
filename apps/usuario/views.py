from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegisterForm
# Create your views here.


class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('mascota:listMascota')
