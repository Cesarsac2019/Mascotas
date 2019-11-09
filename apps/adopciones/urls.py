from apps.adopciones.views import index_adopciones, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete
from django.conf.urls import include, url
from django.shortcuts import redirect
from .import views

urlpatterns = [
    url(r'^index$',index_adopciones),
    url(r'^solicitud/listar$',SolicitudList.as_view(), name='solicitud_listar'),
    url(r'^solicitud/nueva$',SolicitudCreate.as_view(), name='solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)$',SolicitudUpdate.as_view(), name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)$',SolicitudDelete.as_view(), name='solicitud_eliminar'),
]
