# import json
# from rest_framework.views import APIView

# from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf.urls import url
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from apps.usuarios.forms import RegistroForm


# from django.core.urlresolvers import reverse_lazy
#
# from apps.usuarios.forms import RegistroForm
# from apps.usuario.serializers import UserSerializer

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuarios/registrar.html"
	form_class = RegistroForm



#     def get_success_url(self): # override this function if you want to use reverse
#         return reverse('mascota_listar')
# # #
# class UserAPI(APIView):
# 	serializer = UserSerializer
#
# 	def get(self, request, format=None):
# 		lista = User.objects.all()
# 		response = self.serializer(lista, many=True)
#
# 		return HttpResponse(json.dumps(response.data), content_type='application/json')
