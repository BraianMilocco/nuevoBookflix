#Mirar lineas 365 y 367 porque hice cambios de como manejarnos en las views ahora que cambio el modelo de libro

from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
#from .formsu import UserSolicitudForm, RegistrationForm, RegistroTarjeta, CrearPerfil, MailChange, MailConfirmacion, RecuperarCuenta, 
from .formsu import *
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

from random import randint, uniform




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
            tarjeta_usada= CreditCardsUsed(number=numT, cod=codT, date_expiration=dateT, card_name=cardName, bank=bankT, user=cuenta)
            tarjeta_usada.save()
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


def buscarPorIsbs(request, isbn):                       #mmmm me parece que va a tener que estar en el template
    libros = Book.object.filter(isbn=isbn)
    return render(request, welcome, {"libros":libros}) 

def welcome(request):
    publicacion=Billboard.objects.filter(mostrar_en_home=True)
    libros = Book.objects.filter(mostrar_en_home=True)
    libros_cap = BookByChapter.objects.filter(mostrar_en_home=True)
    trailers = Trailer.objects.filter(mostrar_en_home=True)
    historial_libros = StateOfBookByChapter.objects.filter(state="reading") #, profile=request.session.nombrePerfil
    historial_libros_cap = StateOfBook.objects.filter(state="reading")
    return render(request, "bookflix/welcome.html",{'publicaciones':publicacion,"trailers":trailers, "libros":libros, "historial_libros":historial_libros, "historial_libros_cap":historial_libros_cap, "libros_cap":libros_cap}) 

def barra(request):
    return render(request,"bookflix/barra.html", perfil)


def base(request):
    return render(request, "bookflix/base.html")

def perfil(request):
    #Para saber los datos del usuario tenes conectado que usar request.user."atributo"
    #tenes que arreglar todo ahi ese objeto perfil no va a funcionar
    tarjetaActual = CreditCards.objects.get(user =request.user)
    numTarjeta = tarjetaActual.number[-3] + tarjetaActual.number[-2] + tarjetaActual.number[-1]
    return render(request, "bookflix/perfil.html",{'tarjetaActual': tarjetaActual, 'numeroPa': numTarjeta})

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
    solicitudes = UserSolicitud.objects.filter(type_of_solicitud='alta', is_accepted=0)
    usuarios= UserSolicitud.objects.filter(type_of_solicitud='alta', is_accepted=0).values('user')
    tarjetas= CreditCards.objects.filter(user__in= usuarios)
    return render(request,"bookflix/solicitudes.html",{"solicitudes":solicitudes, "tarjetas":tarjetas})
            
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
    publicaciones=len(Billboard.objects.all())
    publicacion=Billboard.objects.filter(id=randint(1,publicaciones+1))
    while not publicacion:
        publicacion=Billboard.objects.filter(id=randint(1,publicaciones+1))

    trailers=len(Trailer.objects.all())
    trailer=Trailer.objects.filter(id=randint(1,(trailers+1)))
    while not trailer:
        trailer=Trailer.objects.filter(id=randint(1,(trailers+1)))

    libros = Book.objects.filter(mostrar_en_home=True)

    return render(request, "bookflix/login.html", {'form': form, 'publicaciones':publicacion, "libros":libros,"trailers":trailer})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/login')


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
            t= CreditCards.objects.get(user= request.user).delete()
            tarjeta= CreditCards(number=numT, cod=codT, date_expiration=dateT, card_name=cardName, bank=bankT, user=request.user)
            tarjeta_vieja = CreditCards.objects.get(user=request.user)
            tarjeta_vieja.delete()
            tarjeta.save()

            tarjeta_usada= CreditCardsUsed(number=numT, cod=codT, date_expiration=dateT, card_name=cardName, bank=bankT, user=request.user)
            try:
                tarjeta_usada_vieja = CreditCardsUsed.objects.get(number=tarjeta.number)
                tarjeta_usada_vieja.delete()
            except CreditCardsUsed.DoesNotExist:
                pass
            tarjeta_usada.save()

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


def cambiar_nombre(request,nombre):
    context={}
    request.session['ErrorDePerfil'] = "1"
    request.session.modified = True
    perfil_anterior = Profile.objects.get(name= nombre, account=request.user)
    if request.POST:
        form= CrearPerfil(request.POST, instance= perfil_anterior)
        if form.is_valid():
            try:
                p= Profile.objects.get(name= form.cleaned_data['name'], account=request.user)
                request.session['ErrorDePerfil'] = "2"
                request.session.modified = True
            except Profile.DoesNotExist:
                perfil_anterior= form.save(commit=False)
                perfil_anterior.account = request.user
                perfil_anterior.save()
                return redirect ('/select_perfil')
    
    form=CrearPerfil()
    context["profile_creation_form"]=form
    return render(request, 'bookflix/cambiar_nombre.html', context)



def solicitar_cambio(request):
    context= { }
    request.session["solicitud"]="1"
    request.session.modified = True
    try:
        cambio_plan =  UserSolicitud.objects.get(is_accepted=0, user=request.user)
        request.session["solicitud"]="0"
        request.session.modified = True
    except UserSolicitud.DoesNotExist: 
        pass
    request.session['ErrorSolicitudCambio']= "Su plan es: " + request.user.plan + ". Si selecciona el mismo no tendrá efecto" 
    request.session.modified = True
    if request.POST:   
        form= UserSolicitudForm(request.POST)
        if form.is_valid():
            planSolicitad= form.cleaned_data['tipo_de_plan']
            if planSolicitad == request.user.plan:
                request.session['ErrorSolicitudCambio']="Qué le dijimos? no puede elegir su plan XD"
                request.session.modified=True
            elif planSolicitad == 'free':
                sol=UserSolicitud(type_of_solicitud='baja', type_of_plan='free', user= request.user)
                sol.save()
                return redirect('/perfil')
            elif planSolicitad == 'normal':
                if request.user.plan == 'free':
                    sol= UserSolicitud(type_of_solicitud='alta', type_of_plan='normal', user= request.user)
                    sol.save()
                else:
                    sol= UserSolicitud(type_of_solicitud='cambio', type_of_plan='normal', user= request.user)
                    sol.save()
                return redirect('/perfil')    
            else:
                if request.user.plan == 'free':
                    sol= UserSolicitud(type_of_solicitud='alta', type_of_plan='premium', user= request.user)
                    sol.save()
                else: 
                    sol= UserSolicitud(type_of_solicitud='cambio', type_of_plan='premium', user= request.user)
                    sol.save()
                return redirect('/perfil') 
    form= UserSolicitudForm()
    context['solicitud'] = form
    return render(request,"bookflix/solicitar_cambio.html", context)

def leer_libro(request,isbn):
     libro= Book.objects.get(isbn = isbn)  #Aca recupero el libro por el isbn para no cambiar el template
     request.session["lectura_otro_perfil"] = False
     if request.user.plan == 'normal':
        try:
            perfil = Profile.objects.exclude(id=request.session["perfil_ayuda"]).get(account=request.user) #aca agrego el isbn al objeto
            try: 
                state = StateOfBook.objects.get(state="reading", profile=perfil, book= libro.id)
                request.session["lectura_otro_perfil"] = True
            except StateOfBook.DoesNotExist:
                pass 
        except Profile.DoesNotExist:
            pass    
        try:
            estado_propio = StateOfBook.objects.get(state="reading", profile=request.session["perfil_ayuda"])
            comenzado = True
        except StateOfBook.DoesNotExist:
            comenzado = False
     libro = Book.objects.get(isbn=isbn)
     return render(request,"bookflix/leer_libro.html",{"libro":libro, "comenzado":comenzado}) 

def leer_libro_por_capitulo(request,isbn):
     libro = BookByChapter.objects.get(isbn=isbn)
     cap_actual = 1
     capitulos=[]
     for i in range (0,libro.cant_chapter): 
        try: 
            Chapter.objects.get(book=libro, number=cap_actual) 
            capitulos.append(Chapter.objects.get(book=libro, number=cap_actual))
            cap_actual = cap_actual + 1
        except Chapter.DoesNotExist: 
            pass
        #capitulos = Chapter.objects.filter(book=libro)
     return render(request,"bookflix/libro_capitulo.html",{"libro":libro, "capitulos":capitulos}) 


def libro_capitulo(request):

    return render(request,"bookflix/libro_capitulo.html")

def libro_por_leer(request,isbn):
    libro = Book.objects.get(isbn=isbn)
    perfil = Profile.objects.get(id=request.session["perfil_ayuda"])
    variable = StateOfBook(state="reading",book=libro, profile=perfil)
    variable.save()
    return render(request,"bookflix/leer_libro.html",{"libro":libro}) 


def libro_cap_por_leer(request,isbn):
    libro = BookByChapter.object.get(isbn=isbn)
    perfil = Profile.object.get(id=request.session["perfil_ayuda"])
    variable = StateOfBookByChapter(state="reading",book=libro, profile=perfil)
    return render(request,"bookflix/libro_por_leer.html", {"libro":libro} )





def historial(request):
     historial_libros = StateOfBook.objects.filter(state="finished")
     historial_libros_cap = StateOfBookByChapter.objects.filter(state="finished")
     #historial = historial_libros_cap |= historial_libros
     sesion = request.session
     return render(request,"bookflix/historial.html",{"historial_libros":historial_libros,"historial_libros_cap":historial_libros_cap, "sesion":sesion }) 



def perfil_seleccionado(request,id_perfil):
    perfil_actual = Profile.objects.get(id=id_perfil)
    perfil_actual.is_active_now = True 
    perfil_actual.save()
    request.session["perfil_ayuda"] = id_perfil

    request.session['nombrePerfil']= perfil_actual.name
    perfil_actual = serializers.serialize("json", Profile.objects.all())
    request.session['perfil_actual']= perfil_actual
    #request.session['perfil_actual']= perfil_actual.name

    request.session.modified = True
    return redirect("/") 


def trailers(request):
    trailers = Trailer.objects.filter(mostrar_en_home=True)
    return render(request,"bookflix/trailers.html",{"trailers":trailers})


class Counter:
       count = 0

       def increment(self):
           self.count += 1
           return ''


def aceptarSolicitud(request,idSol,num):
    try:
        sol= UserSolicitud.objects.get(id=idSol)
        
        if num == '1':
            userSol= UserSolicitud.objects.filter(id=idSol).values('user')
            us= Account.objects.get(id__in=userSol)
            sol.is_accepted= num
            sol.save()
            us.plan= sol.type_of_plan
            us.time_pay=30
            us.date_start_plan= timezone.now()
            us.save()
        else:
            sol.is_accepted=num
            sol.save()
    except UserSolicitud.DoesNotExist:
        pass
    return redirect('/solicitudes')   


def mas_leidos (request):
    libros = StateOfBook.objects.filter(state="reading") #acá tengo que ordenarlos de mayor a menor
    #autores = 
    return render(request,'bookflix/mas_leidos.html', {"libros":libros})





#EScribir views arriba de esta, de acá para abajo nada

#Funciones de automatizacion, escribir cualquier otra view antes que esta

from .funcionesAutomatizacion import *

def simuladorTemporal(request):
    context={}
   #Libros
    try:
        Lib= UpDownBook.objects.filter(up_normal =timezone.now()).values('book')
        li= Book.objects.filter(id__in=Lib)
        cambioNormal(li, True)
        
    except UpDownBook.DoesNotExist:
        pass
    try:
        Lib= UpDownBook.objects.filter(expiration_normal=timezone.now().date()).values('book')         
        li= Book.objects.filter(id__in=Lib)
        cambioNormal(li, False)
    except UpDownBook.DoesNotExist:
        pass
    try:
        Lib= UpDownBook.objects.filter(up_premium =timezone.now()).values('book')
        li= Book.objects.filter(id__in=Lib)
        cambioPremium(li, True)
    except UpDownBook.DoesNotExist:
        pass
    try:
        Lib= UpDownBook.objects.filter(expiration_premium=timezone.now().date()).values('book')         
        li= Book.objects.filter(id__in=Lib)
        cambioPremium(li,False)
    except UpDownBook.DoesNotExist:
        pass

    #LibrosPorCapitulo
    try:
        Lib= UpDownBookByChapter.objects.filter(up_normal =timezone.now()).values('book')
        li= BookByChapter.objects.filter(id__in=Lib)
        cambioNormal(li, True)
    except UpDownBookByChapter.DoesNotExist:
        pass
    try:
        Lib= UpDownBookByChapter.objects.filter(expiration_normal=timezone.now().date()).values('book')         
        li= BookByChapter.objects.filter(id__in=Lib)
        cambioNormal(li, False)
    except UpDownBookByChapter.DoesNotExist:
        pass
    try:
        Lib= UpDownBookByChapter.objects.filter(up_premium =timezone.now()).values('book')
        li= BookByChapter.objects.filter(id__in=Lib)
        cambioPremium(li, True)
    except UpDownBookByChapter.DoesNotExist:
        pass
    try:
        Lib= UpDownBookByChapter.objects.filter(expiration_premium=timezone.now().date()).values('book')         
        li= BookByChapter.objects.filter(id__in=Lib)
        cambioPremium(li,False)
    except UpDownBookByChapter.DoesNotExist:
        pass
    
    #Capitulos

    try:
        cha= UpDownChapter.objects.filter(up =timezone.now()).values('chapter')
        c= Chapter.objects.filter(id__in=cha)
        cambioOtros(c, True )
    except Chapter.DoesNotExist: 
        pass
    try:
        cha= UpDownChapter.objects.filter(expirationl =timezone.now()).values('chapter')
        c= Chapter.objects.filter(id__in=cha)
        cambioOtros(c, False )
    except Chapter.DoesNotExist: pass

    #Novedades

    try:
        cha= UpDownBillboard.objects.filter(up =timezone.now()).values('Billboard')
        c= Billboard.objects.filter(id__in=cha)
        cambioBilTra(c, True )
    except Billboard.DoesNotExist: pass
    try:
        cha= UpDownBillboard.objects.filter(expirationl =timezone.now()).values('Billboard')
        c= Billboard.objects.filter(id__in=cha)
        cambioBilTra(c, False )
    except Billboard.DoesNotExist: pass

    #Trailer

    try:
        cha= UpDownTrailer.objects.filter(up =timezone.now()).values('trailer')
        c= Trailer.objects.filter(id__in=cha)
        cambioBilTra(c, True )
    except Trailer.DoesNotExist: pass
    try:
        cha= UpDownTrailer.objects.filter(expirationl =timezone.now()).values('trailer')
        c= Trailer.objects.filter(id__in=cha)
        cambioBilTra(c, False )
    except Trailer.DoesNotExist: pass

    #Bajas usuarios
    try:
        sol= UserSolicitud.objects.filter(type_of_solicitud='baja').values('user')
        ac= Account.objects.filter(id__in= sol)
        darDeBajaUsuarios(ac)
        context['libros']= ac
    except UserSolicitud.DoesNotExist: pass
    #return render(request, "bookflix/simuladorTemporal.html", context)
    return redirect('/solicitudes')


   