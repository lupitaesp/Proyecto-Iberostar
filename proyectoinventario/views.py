from xml.dom import INVALID_STATE_ERR
from django.http import HttpRequest
from django.shortcuts import redirect, render
from proyectoinventario.forms import FormAssets, FormSalidas
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from proyectoinventario.models import Assets, Clientes


def logi(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Informacion incorrecta")
    form = AuthenticationForm()
    return render(request, "proyectowebapp/index.html", {"form": form})

def home(request):
    bode = Assets.objects.all().filter(accion=0)
    return render(request, "proyectowebapp/home.html", {'bode': bode})

def historial(request):
    cli = Clientes.objects.all()
    return render(request, "proyectowebapp/historial.html",{'cli':cli})

# Filtra en bodega todas las entradas.
def bodega(request):
    bode = Assets.objects.all().filter(accion=1)
    return render(request, "proyectowebapp/bodega.html", {'bode': bode})


def cerrar_sesion(request):
    logout(request)
    return redirect('Login')


def eliminarAsset(request, id_asset):
    bodes = Assets.objects.get(id_asset=id_asset)
    bodes.delete()
    bode = Assets.objects.all().filter(accion=1)
    messages.error(request, "¡Asset eliminado correctamente!")
    return render(request, "proyectowebapp/bodega.html", {'bode': bode, "mensa": 'OK'})


def editarAsset(request, id_asset):
    bodes = Assets.objects.filter(id_asset=id_asset).first()
    form = FormAssets(instance=bodes)
    return render(request, "proyectowebapp/editarAsset.html", {"form": form, 'bodes': bodes})


def actualizarAsset(request, id_asset):
    bodes = Assets.objects.get(id_asset=id_asset)
    form = FormAssets(request.POST, instance=bodes)
    if form.is_valid():
        form.save()
        messages.error(request, "¡Asset actualizado correctamente!")
    bode = Assets.objects.all().filter(accion=1)
    return render(request, "proyectowebapp/bodega.html", {"bode": bode, "mensa": 'OK'})


class FormAssetsView(HttpRequest):

    def inde(request):
        assets = FormAssets()
        return render(request, "proyectowebapp/assetsindex.html", {"form": assets})
# Guardar el formulario

    def procesar_formulario(request):
        assets = FormAssets(request.POST)
        if assets.is_valid():
            assets.save()
            assets = FormAssets()
        return render(request, "proyectowebapp/assetsindex.html", {"form": assets, "mensaje": 'OK'})



class FormAssetsSalidas(HttpRequest):
# Metodo para registrar lo del formulario

    def registrarSalida(request, id_asset):
        dispo = Assets.objects.filter(id_asset=id_asset).first()
        form = FormSalidas(instance=dispo)
        return render(request, "proyectowebapp/assetSalidaForm.html", {"form": form, 'dispo': dispo })
# Guardar el formulario
    def procesarSalida(request, id_asset):
        # ALMACENAMONS EL ID QUE SE OBTIENE DEL POST EN UNA VARIABLE PARA QUE CREE EN LA BASE DE DATOS 
        dispo = Assets.objects.get(id_asset=id_asset)
        nombre=request.POST['nombre']
        email=request.POST['email']
        departamento=request.POST['departamento']
        hotel=request.POST['hotel']
        estado=request.POST['estado']
        descripcion=request.POST['descripcion']
        clientes = Clientes.objects.create(asset=dispo,nombre=nombre,email=email,departamento=departamento,hotel=hotel,estado=estado,descripcion=descripcion)
        clientes.save()
        messages.error(request, "¡Usuario asignado correctamente!")
        return render(request, "proyectowebapp/home.html", {"form": clientes, "mensaje": 'OK'})
