from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from web.models import *
from algoritm import *

def inicio(request):
    return render_to_response('Inicio.html')


def lista_productos(request):
    productos = Item.objects.all()
    return render_to_response('lista_productos.html',{'productos':productos}, context_instance=RequestContext(request))

def lista_usuarios(request):
    usuarios = WebUser.objects.all()
    return render_to_response('lista_usuarios.html',{'usuarios':usuarios}, context_instance=RequestContext(request))

def recomendaciones(request):
    diccionario = dictionary()
    recomendacion = {}
    
    print diccionario
    
    for user in diccionario:
        rec = getRecommendations(diccionario, user,similarity=sim_pearson)
        recomendacion[user] = rec
      
    return render_to_response('recomendaciones.html',{'recomendacion':recomendacion}, context_instance=RequestContext(request))
    