from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder para editar el blog numero: {number}")

def destroy(request, number):
    return redirect('/blogs')

def json(request): 
    return JsonResponse({'título': 'Este Es El Título'})


##def index(request):
##    return HttpResponse("¡Hola, mundo!")
##
##
##def adiós(request):
##    return HttpResponse("¡Chao pescao!")
##
##def saludar(request, nombre):
##    return HttpResponse("¡Hola, " + nombre + '!')

