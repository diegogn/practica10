from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from web.models import *
from algoritm import *
from forms import *

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
    itemMatch = calculateSimilarItems(diccionario, 10)
    recomendacion = {}
    
    print diccionario
    
    for user in diccionario:
        rec = getRecommendedItems(diccionario, itemMatch,user)
        recomendacion[user] = rec[0:2]
      
    return render_to_response('recomendaciones.html',{'recomendacion':recomendacion}, context_instance=RequestContext(request))

def recomendaciones_busqueda(request):
    if request.method == 'POST':
        form = BuscaRecomendacion(request.POST)
        if form.is_valid():
            diccionario = dictionary()
            itemMatch = calculateSimilarItems(diccionario, 10)
            user = form.cleaned_data['choices']
            recs = getRecommendedItems(diccionario, itemMatch,user)
            return render_to_response('recomendaciones_busqueda.html',{'recs':recs[0:2],'form':form,'user':user},context_instance=RequestContext(request))
    else:
        usuarios = WebUser.objects.all()
        form = BuscaRecomendacion()
        
    return render_to_response('formulariorecomendaciones_busqueda.html',{'formulario':form,'usuarios':usuarios},context_instance=RequestContext(request))    