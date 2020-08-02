from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.mascota.views import index, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, MascotaAPI

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', login_required(MascotaCreate.as_view()), name='createMascota'),
    path('list/', login_required(MascotaList.as_view()), name='listMascota'),
    re_path(r'^edit/(?P<pk>[\d])/$',
            login_required(MascotaUpdate.as_view()), name='editMascota'),
    re_path(r'^delete/(?P<pk>[\d])/$',
            login_required(MascotaDelete.as_view()), name='delMascota'),
    path('api/list', MascotaAPI.as_view(), name='apiList'),

]
