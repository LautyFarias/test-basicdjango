from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm
# Create your views here.


def index(request):
    return HttpResponse("Adopcion")


class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/list.html'


class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopcion/form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('adopcion:listSolicitud')

    def get_context_data(self, **kwargs):
        contexto = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in contexto:
            contexto['form'] = self.form_class(self.request.GET)
        if 'form2' not in contexto:
            contexto['form2'] = self.second_form_class(self.request.GET)
        return contexto

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class SolicitudUpdate(UpdateView):
    model = Solicitud
    second_model = Persona
    template_name = 'adopcion/form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('adopcion:listSolicitud')

    def get_context_data(self, **kwargs):
        contexto = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        if 'form' not in contexto:
            contexto['form'] = self.form_class()
        if 'form2' not in contexto:
            contexto['form2'] = self.second_form_class(instance=persona)
        contexto['id'] = pk
        return contexto

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        form = self.form_class(request.POST, instance=solicitud)
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'adopcion/delete.html'
    success_url = reverse_lazy('adopcion:listSolicitud')