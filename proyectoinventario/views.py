from django.http import HttpRequest
from django.shortcuts import render
from proyectoinventario.forms import FormAssets

def login(request):
    return render(request,"proyectowebapp/index.html")

def home(request):
    return render(request,"proyectowebapp/home.html")

def bodega(request):
    return render(request,"proyectowebapp/bodega.html")


class FormAssetsView(HttpRequest):

    def inde(request):
        assets = FormAssets()
        return render(request, "proyectowebapp/assetsindex.html", {"form": assets})

    def procesar_formulario(request):
        assets = FormAssets(request.POST)
        if assets.is_valid():
            assets.save()
            assets = FormAssets()
        return render(request,"proyectowebapp/assetsindex.html", {"form": assets, "mensaje": 'OK'})
        




# Create your views here.
