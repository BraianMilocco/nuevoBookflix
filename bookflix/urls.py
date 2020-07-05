from django.urls import path, include
from .views import * 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    path('', welcome, name='welcome'),
    url('login/', login_propio, name='login'),
    path('logout/', logout, name='logout'),#no se para que son los names pero por las duda los dejo
    path('register_page/', register_page, name='registrar'),
    path('select_perfil/', select_perfil, name='seleccionarPerfil'),
    path("perfil/", perfil, name='perfil'),
    path("cambiar_contrasenia/", cambiar_contrasenia, name="cambiar_contrasenia"),
    path("cambiar_tarjeta/", cambiar_tarjeta, name="cambiar_tarjeta"),
    path("cambiar_email/", cambiar_email, name="cambiar_email"),
    path("publicacion/<titulo>/", publicacion, name="publicacion"),
    path("publicaciones/", publicaciones, name="publicaciones"),
    path('crear_perfil/', crear_perfil, name='crear_perfil'),
    path('confirmarCuenta/', confirmarCuenta, name='confirmarCuenta'),
    path('solicitudes/', solicitudes, name='solicitudes'),
    path('solicitar_cambio/', solicitar_cambio, name='solicitar_cambio'),
    path('recuperarCuenta/', recuperarCuenta, name='recuperarCuenta'),
    path('leer_libro/<isbn>/', leer_libro, name='leerlibro'),
    path('libro_capitulo/<isbn>/', leer_libro_por_capitulo, name='libro_capitulo'),
    path('libro_capitulo/', libro_capitulo, name='libro_capitulo'), 
    path("perfil_seleccionado/<id_perfil>/", perfil_seleccionado, name="perfil_seleccionado"),  
    path("simuladorTemporal/", simuladorTemporal, name="simuladorTemporal"),
    path("trailers/", trailers, name="trailers"),
    path("aceptarSolicitud/<idSol>/<num>/", aceptarSolicitud, name="aceptarSolicitud"),
    #path("buscar/",buscar, name="buscar"),
    path("historial/", historial, name="historial"), 
    path("libro_por_leer/<isbn>/", libro_por_leer, name="libro_por_leer"), 
    path("mas_leidos/", mas_leidos, name="mas_leidos"), 
    path('cambiar_nombre/<nombre>/', cambiar_nombre, name='cambiar_nombre'),
    path('mostrar_tiempos/', mostrar_tiempos, name='mostrar_tiempos'),
    path('comentar/<isbn>/', escribirComentario, name="escribirComentario"),
    path('verComentario/<id>/', verComentario, name="vercomentario"),
    path('denunciarComentario/<id>/<isbn>/', denunciarComentario, name="denunciarComentario"),
    path('comentariosDenunciados/', comentariosDenunciados, name="comentariosDenunciados"),
    path('denuncia/<id>/<boole>/<n>/', denuncia, name="denuncia"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)