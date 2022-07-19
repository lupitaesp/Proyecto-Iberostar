from django.shortcuts import render, HttpResponse

def login(request):
    return render(request,"proyectowebapp/index.html")

def home(request):
    return render(request,"proyectowebapp/home.html")

def tablero(request):
    return render(request,"proyectowebapp/tablero.html")





# Create your views here.
