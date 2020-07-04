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
from .models import Account, UserSolicitud

def darDeBajaUsuarios(objectAccounts):

    for acc in objectAccounts:
        if timezone.now().date() == (acc.date_start_plan + datetime.timedelta(days=acc.time_pay)):
            acc.plan = 'free'
            acc. time_pay = 0
            acc.save()

