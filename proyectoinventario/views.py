from django.http import HttpRequest
from django.shortcuts import redirect, render
from proyectoinventario.forms import FormAssets
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from proyectoinventario.models import Assets

def logi(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario= form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request,"Usuario no valido")
        else: 
            messages.error(request,"Informacion incorrecta")
    form=AuthenticationForm()
    return render(request,"proyectowebapp/index.html", {"form":form})

def home(request):
    return render(request,"proyectowebapp/home.html")

#Filtra en bodega todas las entradas.
def bodega(request):
    bode = Assets.objects.all().filter(accion=1)
    return render(request,"proyectowebapp/bodega.html", {'bode': bode})

def cerrar_sesion(request):
    logout(request)
    return redirect('Login')

def eliminarAssets(request, id):
    bodes=Assets.objects.get(id=id)
    bodes.delete()
    bode = Assets.objects.all().filter(accion=1)
    messages.error(request,"¡Asset eliminado correctamente!")
    return render(request,"proyectowebapp/bodega.html", {'bode': bode, "mensaje": 'OK'})

def editarAsset(request, id):
    bodes = Assets.objects.filter(id=id).first()
    form = FormAssets(instance=bodes)
    return render(request, "proyectowebapp/editarAsset.html", {"form": form, 'bodes':bodes})

def actualizarAsset(request, id):
    bodes = Assets.objects.get(id=id)
    form = FormAssets(request.POST, instance=bodes)
    if form.is_valid():
        form.save()
        messages.error(request,"¡Asset actualizado correctamente!")
    bode = Assets.objects.all()

    return render(request, "proyectowebapp/bodega.html", {"bode": bode})

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
        
