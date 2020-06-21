from django import forms
from .models import Account, CreditCards, Profile, ConfirmationMail, Chapter, BookByChapter, UserSolicitud
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms import ValidationError
from datetime import datetime, timedelta
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField
from .models import Author, Editorial, Gender

class UserSolicitudForm(forms.Form):
    CHOICESS= GEEKS_CHOICES =( 
    ("free", "free"), 
    ("normal", "normal"), 
    ("premium", "premium"), )

    tipo_de_plan= forms.ChoiceField(label="Seleccione Plan", choices=CHOICESS, )


class MailConfirmacion(forms.Form):
    codigoV = forms.CharField(label='codigo Validacion')


class RegistroTarjeta(forms.Form):
  
    number = CardNumberField(label='numero', error_messages = {'invalid': 'La tarjeta debe tener entre 12 y 16 numeros'})
    date_expiration = CardExpiryField(label='fecha de vencimiento', error_messages = {'date_passed': 'Fecha Invalida', } )
    cod = SecurityCodeField(label='CVV/CVC', error_messages = {'invalid': 'Código inválido'},)
    card_name = forms.CharField( max_length=50, label='nombre en Tarjeta')
    bank = forms.CharField(max_length=50, label='banco')
    

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Account
        fields = (  
            'username',
            'email',
            'password1',
            'password2',            
        )

class CrearPerfil(ModelForm):
    class Meta: 
        model = Profile
        fields = ('name',)


class MailChange(ModelForm):

    class Meta: 
        model = Account
        fields = ('email',)
    



    def clean_email(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            try:
                account= Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError("el mail se encuentra en uso" )

class RecuperarCuenta(forms.Form):
    email= forms.EmailField()
    


class ChapForm(ModelForm):
    class Meta:
        model = Chapter
        exclude = ['id', ]

    def clean(self):
        n = self.cleaned_data['number']
        b = self.cleaned_data['book']
        try:
            book= BookByChapter.objects.get(isbn= b)
            if n > book.cant_chapter:
                raise forms.ValidationError("Product offer price cannot be greater than Product MRP.")
            else:
                return self.cleaned_data
        except BookByChapter.DoesNotExist:
            return self.cleaned_data


class busquedaOtrosForm(forms.Form):
    def createDict(anQueryss):
        dict= [("seleccione", "seleccione"),]

        for i in anQueryss:
            dict.append((i, i))
        return dict
    
    aut= Author.objects.all()
    edi= Editorial.objects.all()
    gen= Gender.objects.all()

    ChAut=createDict(aut)
    chEdi=createDict(edi)
    chGen=createDict(gen)
    
    isbn= forms.CharField(label="Buscar Por ISBN", max_length=16, required=False,)
    titulo= forms.CharField( max_length= 70, required=False)
    genero= forms.ChoiceField(choices=chGen, required=False)
    autor= forms.ChoiceField( choices=ChAut, required=False)
    editorial=forms.ChoiceField( choices=chEdi, required=False)

    def clean(self):
        cleaned_data = self.cleaned_data

        if not cleaned_data['isbn'].isalnum():
            raise ValidationError('Ese no es un isbn valido')
        else:
            return cleaned_data