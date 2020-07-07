def cambioNormal(lista, bool):
    for l in lista:
        l.on_normal= bool
        l.save()

def cambioPremium(lista, bool):
    for l in lista:
        l.on_premium= bool
        l.save()
def cambioOtros(lista, bool):
    for l in lista:
        l.active=bool
        l.save()
def cambioBilTra(lista, bool):
    for l in lista:
        l.mostrar_en_home=bool
        l.save()

import datetime
from django.utils import timezone
from .models import Account, UserSolicitud, StateOfBook, StateOfBookByChapter, Book, BookByChapter, Gender, Editorial, Author

def darDeBajaUsuarios(objectAccounts):

    for acc in objectAccounts:
        if timezone.now().date() == (acc.date_start_plan + datetime.timedelta(days=acc.time_pay)):
            acc.plan = 'free'
            acc. time_pay = 0
            acc.save()
            
from random import randint, uniform


def randomCood(num):
    unique_id = random.randint(0,(num-1))
    return unique_id

def recomendados(perfil):
    try:
        estados= StateOfBook.objects.filter(profile=perfil, state='finished').values('book')
        libros_leidos=[]
        for i in estados:
            libros_leidos.append(Book.objects.filter(id__in=i))
        libroARandom= libros_leidos[randomCood(len(libros_leidos))]

        #queSeleccionar= randomCood(9)

        #if queSeleccionar == 0 or queSeleccionar == 1 or queSeleccionar==2 or queSeleccionar==3:
        generos= libroARandom.genders.all()
        aux= [ ]
        for genero in generos:
            aux.append(genero)
        genero= aux[randomCood(len(aux))]
        librosConEseGenero= Book.objects.exclude(id__in=libros_leidos.id).filter(genders=genero)
        if len(librosConEseGenero)>0:
            return librosConEseGenero[randomCood(len(librosConEseGenero))]

        #elif queSeleccionar == 4 or queSeleccionar==5 or queSeleccionar==6:
        
        #else:


    except:
        return Book.objects.all()


#def recomendadosCapitulo(perfil):