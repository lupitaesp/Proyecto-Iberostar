from django.urls import path
from proyectoinventario import views

urlpatterns = [
    path('',views.login,name="Log in"),
    path('home',views.home,name="Home"),
    path('tablero',views.tablero,name="Tablero"),
]
