from django.conf.urls import url, include
from apps.ninios.views import listar,index, ninio_view, ninio_list, ninio_edit, ninio_delete
from django.shortcuts import redirect
from . import views


urlpatterns = [
    url(r'^$', views.listar, name = 'listado'),
    url(r'^nuevo$', ninio_view, name="ninio_crear"),
    url(r'^listar$', ninio_list, name="ninio_listar"),
    url(r'^editar/(?P<id_ninio>\d+)/$', ninio_edit, name='ninio_edit'),
    url(r'^eliminar/(?P<id_ninio>\d+)/$', ninio_delete, name='ninio_eliminar'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^adopciones/', include('apps.adopciones.urls', namespace = "adopciones")),

]
