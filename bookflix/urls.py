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
    path("publicaciones/", publicaciones, name="publicaiones"),
    path('crear_perfil/', crear_perfil, name='crear_perfil'),
    path('confirmarCuenta/', confirmarCuenta, name='confirmarCuenta'),
    path('solicitudes/', solicitudes, name='solicitudes'),
    path('solicitar_cambio/', solicitar_cambio, name='solicitar_cambio'),
    path('recuperarCuenta/', recuperarCuenta, name='recuperarCuenta'),
    path('leer_libro/<isbn>/', leer_libro, name='leerlibro'),
    path('libro_capitulo/', libro_capitulo, name='libro_capitulo'), 
    path("perfil_seleccionado/<id_perfil>/", perfil_seleccionado, name="perfil_seleccionado"),  
    path("simuladorTemporal/", simuladorTemporal, name="simuladorTemporal"),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)