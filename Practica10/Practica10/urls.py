from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'web.views.inicio'),
    url(r'^lista_productos/', 'web.views.lista_productos'),
    url(r'^lista_usuarios/', 'web.views.lista_usuarios'),
    url(r'^recomendaciones/', 'web.views.recomendaciones'),
    url(r'^recomendaciones_busqueda/', 'web.views.recomendaciones_busqueda'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
