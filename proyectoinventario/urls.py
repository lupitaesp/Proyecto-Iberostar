from django.urls import path
from proyectoinventario import views


urlpatterns = [
    path('',views.logi,name="Login"),
    path('home',views.home,name="Home"),
    path('bodega',views.bodega,name="Bodega"),
   # path('dispositivos',views.dispositivos,name="Dispositivos"),
    path('registrarAsset/', views.FormAssetsView.inde, name='registrarAsset'),
    path('guardarAsset/',  views.FormAssetsView.procesar_formulario, name='guardarAsset'),
]
