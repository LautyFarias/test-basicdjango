from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core import serializers
from rest_framework.views import APIView
import json
from apps.mascota.serializers import MascotaSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
# Create your views here.


def index(request):
    return render(request, 'mascota/index.html')


# def listado(request):
#     lista = serializers.serialize('json', Mascota.objects.all(), fields=['nombre','sexo'])
#     return HttpResponse(lista)

# def mascota_form(request):
#     if request.method == 'POST':
#         form = MascotaForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('mascota:index')
#     else:
#         form = MascotaForm()
#     return render(request, 'mascota/form.html', {'form': form})


# def mascota_list(request):
#     mascotas = Mascota.objects.all().order_by('id')
#     contexto = {'mascotas': mascotas}
#     return render(request, 'mascota/list.html', contexto)


# def mascota_edit(request, id_mascota):
#     mascota = Mascota.objects.get(id=id_mascota)
#     if request.method == 'GET':
#         form = MascotaForm(instance=mascota)
#     else:
#         form = MascotaForm(request.POST, instance=mascota)
#         if form.is_valid():
#             form.save()
#         return redirect('mascota:listMascota')
#     return render(request, 'mascota/form.html', {'form': form})


# def mascota_delete(request, id_mascota):
#     mascota = Mascota.objects.get(id=id_mascota)
#     if request.method == 'POST':
#         mascota.delete()
#         return redirect('mascota:listMascota')
#     return render(request, 'mascota/delete.html', {'mascota': mascota})


class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/list.html'
    paginate_by = 2


class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/form.html'
    success_url = reverse_lazy('mascota:listMascota')


class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/form.html'
    success_url = reverse_lazy('mascota:listMascota')


class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/delete.html'
    success_url = reverse_lazy('mascota:listMascota')


class MascotaAPI(APIView):
    serializer = MascotaSerializer

    def get(self, request, format=None):
        lista = Mascota.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')
