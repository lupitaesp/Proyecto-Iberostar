from django.urls import path
from proyectoinventario import views
from .views import actualizarAsset, cerrar_sesion
from .views import eliminarAsset
from .views import editarAsset


urlpatterns = [
    path('',views.logi,name="Login"),
    path('home',views.home,name="Home"),
    path('bodega',views.bodega,name="Bodega"),
    path('historial',views.historial,name="Historial"),

   # path('dispositivos',views.dispositivos,name="Dispositivos"),
    path('registrarAsset/', views.FormAssetsView.inde, name='registrarAsset'),
    path('guardarAsset/',  views.FormAssetsView.procesar_formulario, name='guardarAsset'),
    path('cerrar_sesion',  cerrar_sesion, name='cerrar_sesion'), 
    path('eliminarAsset/<int:id>',  eliminarAsset, name='eliminarAsset'),
    path('editarAsset/<int:id>',  editarAsset, name='editarAsset'),
    path('actualizarAsset/<int:id>',  actualizarAsset, name='actualizarAsset'),
    path('registrarSalida/<int:id>', views.FormAssetsSalidas.registrarSalida, name='registrarSalida'),
    path('guardarSalida/',  views.FormAssetsSalidas.procesarSalida, name='guardarSalida'),

] 
