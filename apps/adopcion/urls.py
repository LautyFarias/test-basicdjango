from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.adopcion.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    path('', index, name='index'),
    path('solicitud/list', login_required(SolicitudList.as_view()),
         name='listSolicitud'),
    path('solicitud/nuevo', login_required(SolicitudCreate.as_view()),
         name='createSolicitud'),
    re_path(r'^solicitud/edit/(?P<pk>[\d])/$',
            login_required(SolicitudUpdate.as_view()), name='editSolicitud'),
    re_path(r'^solicitud/del/(?P<pk>[\d])/$',
            login_required(SolicitudDelete.as_view()), name='delSolicitud'),
]
