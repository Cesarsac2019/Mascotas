
from django.shortcuts import render, redirect

from apps.ninios.forms import NinioForm
from apps.ninios.models import Ninio


def index(request):
    return render(request, 'ninios/index.html')

def listar(request):
    p = Ninio.objects.all()
    return render(request, 'ninios/ninios_list.html', {'p':p})

def ninio_view(request):
    if request.method == 'POST':
        form = NinioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ninio_listar')
    else:
        form = NinioForm()

    return render(request, 'ninios/ninios_form.html', {'form':form})

def ninio_list(request):
	ninio = Ninio.objects.all().order_by('id')
	contexto = {'ninios':ninio}
	return render(request, 'ninios/ninios_list.html', contexto)

def ninio_edit(request, id_ninio):
	ninio = Ninio.objects.get(id=id_ninio)
	if request.method == 'GET':
		form = NinioForm(instance=ninio)
	else:
		form = NinioForm(request.POST, instance=ninio)
		if form.is_valid():
			form.save()
		return redirect('ninio_listar')
	return render(request, 'ninios/ninios_form.html', {'form':form})


def ninio_delete(request, id_ninio):
	ninio = Ninio.objects.get(id=id_ninio)
	if request.method == 'POST':
		ninio.delete()
		return redirect('ninio_listar')
	return render(request, 'ninios/ninios_delete.html', {'ninio':ninio})
