from django.urls import path
from proyectoinventario import views
from .views import cerrar_sesion

urlpatterns = [
    path('',views.logi,name="Login"),
    path('home',views.home,name="Home"),
    path('bodega',views.bodega,name="Bodega"),
   # path('dispositivos',views.dispositivos,name="Dispositivos"),
    path('registrarAsset/', views.FormAssetsView.inde, name='registrarAsset'),
    path('guardarAsset/',  views.FormAssetsView.procesar_formulario, name='guardarAsset'),
    path('cerrar_sesion',  cerrar_sesion, name='cerrar_sesion'), 
] 
