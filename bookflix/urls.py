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
    path("buscar/",buscar, name="buscar"),
    path("historial/", historial, name="historial"), 
    path("libro_por_leer/<isbn>/", libro_por_leer, name="libro_por_leer"), 
    path("mas_leidos/", mas_leidos, name="mas_leidos"), 
    path('cambiar_nombre/<nombre>/', cambiar_nombre, name='cambiar_nombre'),
    path('mostrar_tiempos/', mostrar_tiempos, name='mostrar_tiempos'),
    path('comentar/<isbn>/', escribirComentario, name="escribirComentario"),
    path('verComentario/<id>/<deDonde>', verComentario, name="vercomentario"),
    path('denunciarComentario/<id>/<isbn>/', denunciarComentario, name="denunciarComentario"),
    path('comentariosDenunciados/', comentariosDenunciados, name="comentariosDenunciados"),
    path('denuncia/<id>/<boole>/<n>/', denuncia, name="denuncia"),
    path('agregar_libro_favoritos/<isbn>', agregar_libro_favoritos, name='agregar_libro_favoritos'),
    path('quitar_libro/<isbn>', quitar_libro, name='quitar_libro'),
    path('agregar_futuras_lecturas/<isbn>', agregar_futuras_lecturas, name='agregar_futuras_lecturas'),
    path('quitar_futuras_lecturas/<isbn>', quitar_futuras_lecturas, name='quitar_futuras_lecturas'),
    path('listar_favoritos/', listar_favoritos, name='listar_favoritos'),
    #path('puntuar_libro/<puntuacion>/<isbn>', puntuar_libro, name='puntuar_libro'),
    path('vermiscomentarios/', vermiscomentarios, name="vermiscomentarios"),
    path('borrarcomentario/<id>/<isbn>/<aux>', borrarcomentario, name="borrarcomentario"),
    path('puntuar/<isbn>/<tipo>/<puntos>', puntuar, name="puntuar"),
    path('misvotos/', misvotos, name="misvotos"),
    path('estadisticas/', stats, name="stats"),
    path('estadisticas/<queEs>', estadisticas, name="estadisticas"),
    path('agregar_a_leyendo/<isbn>', agregar_a_leyendo, name="agregar_a_leyendo"),
    path('quitar_de_leyendo/<isbn>', quitar_de_leyendo, name="quitar_de_leyendo"),
    path('terminar_libro/<isbn>', terminar_libro, name="terminar_libro"),
    path('quitar_terminado/<isbn>', quitar_terminado, name="quitar_terminado"),
    path('borrar_perfil/<perfil>', borrar_perfil, name="borrar_perfil"),
    path('borrar_perfil_definitivo/<perfil>', borrar_perfil_definitivo, name="borrar_perfil_definitivo"),
    path('borrar_cuenta/', borrar_cuenta, name="borrar_cuenta"),
    path('borrar_cuenta_definitivo/', borrar_cuenta_definitivo, name="borrar_cuenta_definitivo"),


] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)