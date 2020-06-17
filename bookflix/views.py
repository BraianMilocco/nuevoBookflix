from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import RegistrationForm, RegistroTarjeta, CrearPerfil, MailChange, MailConfirmacion, RecuperarCuenta
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import shortcuts
from bookflix.models import Billboard, Profile, CreditCards, Account
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from ing2.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.conf import settings

from django.utils.crypto import get_random_string

from django.core import serializers

#codigo de mail
#do_login(request, user)
#                send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
#         ['completar@gmail.com'])

def randomCod(num):
    unique_id = get_random_string(length=num)
    return unique_id



def register_page(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        formCard = RegistroTarjeta(request.POST)
        # Si el formulario es válido...
        if form.is_valid() and formCard.is_valid():  

            # Creamos la nueva cuenta de usuario
            cuenta= form.save()
            id_account= form.cleaned_data.get('id')
            email= form.cleaned_data.get('email')
            raw_password= form.cleaned_data.get('password1')
            #account = authenticate(email=email, password=raw_password)
            
            numT= formCard.cleaned_data.get("number")
            codT= formCard.cleaned_data.get("cod")
            dateT= formCard.cleaned_data.get("date_expiration")
            cardName= formCard.cleaned_data.get("card_name")
            bankT=formCard.cleaned_data.get("bank")

            tarjeta= CreditCards(number=numT, cod=codT, date_expiration=dateT, card_name=cardName, bank=bankT, user=cuenta)
            tarjeta.save()
            #enviar mail confirmacion
            codillo = randomCod(10)
            send_mail('Aquí tiene su codigo de confirmacion', codillo, settings.EMAIL_HOST_USER,[email])

            confir= ConfirmationMail(mail=email, codigo=codillo, tipo=1 )
            confir.save()
            request.session['emailConfirm']= email
            request.session.modified = True
            return redirect('/confirmarCuenta')
        else:
            context["user_creation_form"]=form
            context["creacion_tarjeta"]= formCard
            #context["profile_creation_form"]=formPerfil
    else:
        form=RegistrationForm()
        formCard=RegistroTarjeta()
        formPerfil= CrearPerfil()
        context["user_creation_form"]=form
        context["creacion_tarjeta"]=formCard
        context["profile_creation_form"]=formPerfil
    return render(request, 'bookflix/register_page.html', context)


def confirmarCuenta(request):
    context={}
    if request.POST :
        form= MailConfirmacion(request.POST, )
        em= request.session['emailConfirm']
        confirmations= ConfirmationMail.objects.get( mail = em)
        
        if  form.is_valid():
            codEntrado = form.cleaned_data.get("codigoV")
            if confirmations.codigo == codEntrado:
                
                usuario=  Account.objects.get(email = em)
                usuario.confirmo = True
                usuario.save()
                send_mail('Registro Confirmado', 'bienvenido a la familia', settings.EMAIL_HOST_USER,[usuario.email])
                
                confirmations.delete()
  
                return redirect('/login')
            else:
                messages.error(request, 'codigo erroneo')
    else:
        form= MailConfirmacion()
    context["confirmacion"]= form 
    return render(request, "bookflix/confirmacion.html", context)


def buscarPorAutor(request, autor):                       #mmmm me parece que va a tener que estar en el template
    libros = Book.object.filter(Author=autor)
    return render(request, welcome, {"libros":libros}) 

def welcome(request):
    publicacion=Billboard.objects.filter(mostrar_en_home=True)
    libros = Book.objects.filter(mostrar_en_home=True)
    trailers = Trailer.objects.filter(mostrar_en_home=True)
    return render(request, "bookflix/welcome.html",{'publicaciones':publicacion,"trailers":trailers, "libros":libros}) 

def barra(request):
    return render(request,"bookflix/barra.html", perfil)


def base(request):
    return render(request, "bookflix/base.html")

def perfil(request):
    #Para saber los datos del usuario tenes conectado que usar request.user."atributo"
    #tenes que arreglar todo ahi ese objeto perfil no va a funcionar
    tarjetaActual = CreditCards.objects.get(user =request.user)
    return render(request, "bookflix/perfil.html",{'tarjetaActual': tarjetaActual})

def publicaciones(request):
    publicacion=Billboard.objects.filter(mostrar_en_home=True)
    return render(request, "bookflix/publicaciones.html",{'publicaciones':publicacion, })


def publicacion(request, titulo):
    publicacion=Billboard.objects.get(title=titulo)
    return render(request, "bookflix/publicacion.html",{"publicacion":publicacion})

def select_perfil(request):
    perfiles = Profile.objects.filter(account = request.user)
   
    return render(request, "bookflix/select_perfil.html", {'perfiles': perfiles,}) #"tarjetaActual": tarjetaActual, "perfilActual":perfilActual})

def solicitudes(request):
    solicitudes = UserSolicitud.objects.filter()
    return render(request,"bookflix/solicitudes.html",{"solicitudes":solicitudes})
            
def login_propio(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password,)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente  Y le redireccionamos a la portada
                if user.confirmo:
                    do_login(request, user)
                    return redirect('/select_perfil')
                request.session['emailConfirm']= user.email
                request.session.modified = True
                return redirect('/confirmarCuenta')
                
            
    # Si llegamos al final renderizamos el formulario
    publicacion=Billboard.objects.filter(mostrar_en_home=True)
    libros = Book.objects.filter(mostrar_en_home=True)

    return render(request, "bookflix/login.html", {'form': form, 'publicaciones':publicacion, "libros":libros,})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/login')




# Desde acá van todos los "cambiar algo"




def cambiar_contrasenia(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Su Contrasenia fue cambiada con exito')
            send_mail('Cambio contraseña exitoso Bookflix', "su nueva contrasena es: ... recordala!! no te lo vamos a decir", settings.EMAIL_HOST_USER,[request.user.email])            
            return redirect('/perfil')
        else:
            messages.error(request, 'Corrija el error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "bookflix/cambiar_contraseña.html", {
        'form': form
    })

def cambiar_tarjeta(request):
    
    if request.method == 'POST':
        form = RegistroTarjeta(request.POST)
        if form.is_valid():
            numT= form.cleaned_data.get("number")
            codT= form.cleaned_data.get("cod")
            dateT= form.cleaned_data.get("date_expiration")
            cardName= form.cleaned_data.get("card_name")
            bankT=form.cleaned_data.get("bank")

            tarjeta= CreditCards(number=numT, cod=codT, date_expiration=dateT, card_name=cardName, bank=bankT, user=request.user)
            tarjeta.save()
            return redirect('/perfil')      
        else:
            messages.error(request, 'error tarjeta')
    else:
        form=RegistroTarjeta()
    return render(request, "bookflix/cambiar_tarjeta.html", {'form': form})


def cambiar_email(request):
    context={}
    mm= request.user.email
    if request.POST:
        form= MailChange(request.POST, instance= request.user)
        if form.is_valid():
            mensaje= "El nuevo mail de la cuenta deja dee ser este, para ser " + form.cleaned_data['email'] + ". En caso de no ser usted, responder a este mail dentro de las 48hs recibido con el asunto 'yo no hice el cambio' "
            send_mail('Cambio de Mail Bookflix', mensaje, settings.EMAIL_HOST_USER,[mm])
            form.save()
            send_mail('Nuevo Mail Bookflix', "mensaje de confirmacion del cambio de mail", settings.EMAIL_HOST_USER,[request.user.email])            
            return redirect('/perfil')
        else:
            messages.error(request, 'mail en uso')
    else:
        form= MailChange(
            initial={
                "email": request.user.email,
            }
        )
    context["cambio_mail"]= form 
    return render(request, "bookflix/cambiar_email.html", context)

def recuperarCuenta(request):
    context={}
    if request.POST: 
        form= RecuperarCuenta(request.POST)
        if form.is_valid():
            mail= form.cleaned_data['email']
            try:
                aco = Account.objects.get(email=mail)
                contrasena= randomCod(12)
                aco= Account.objects.get(email=mail)
                aco.set_password(contrasena)
                aco.save()
                send_mail('Recuperacion cuenta Bookflix', "su nueva contrasena es: "+ contrasena + " podes cambiarla desde tu perfil", settings.EMAIL_HOST_USER,[mail])            
                return redirect('/login')
            except Account.DoesNotExist:
                messages.error(request, 'mail no existe')
    else: 
        form= RecuperarCuenta()
        context['recupero']= form
    return render(request, "bookflix/recuperarCuenta.html", context)

def crear_perfil(request):
    context={}
    request.session['ErrorDePerfil'] = "1"
    request.session.modified = True
    if request.POST:
        form= CrearPerfil(request.POST)
        if form.is_valid():
            try:
                p= Profile.objects.get(name= form.cleaned_data['name'], account=request.user)
                request.session['ErrorDePerfil'] = "2"
                request.session.modified = True
            except Profile.DoesNotExist:
                perfil= form.save(commit=False)
                perfil.account = request.user
                perfil.save()
                return redirect ('/select_perfil')
    
    form=CrearPerfil()
    context["profile_creation_form"]=form
    return render(request, 'bookflix/crear_perfil.html', context)

def solicitar_cambio(request):
     return render(request,"bookflix/solicitar_cambio.html")

def leer_libro(request,isbn):
     libro = Book.objects.get(isbn=isbn)
     return render(request,"bookflix/leer_libro.html",{"libro":libro}) 


def libro_capitulo(request):

    return render(request,"bookflix/libro_capitulo.html") 


def perfil_seleccionado(request,id_perfil):
    perfil_actual = Profile.objects.get(id=id_perfil)
    perfil_actual.is_active_now = True 
    perfil_actual.save()
    request.session['nombrePerfil']= perfil_actual.name
    perfil_actual = serializers.serialize("json", Profile.objects.all())
    request.session['perfil_actual']= perfil_actual
    #request.session['perfil_actual']= perfil_actual.name
    return redirect("/") 

