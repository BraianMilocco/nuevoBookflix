from django.db import models
from django.core.exceptions import FieldError, ValidationError
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from datetime import datetime, timedelta
from django.utils import timezone
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField




#Probando, va a quedar un choclo gigante con todos los objetos aca
#Orden Author-> Gender-> Editorial-> CreditCards-> Account-> Profile->  
# Publication (y sus hijos)-> StateOfBook-> Comment -> Like -> LikeComment -->>
# -> ExpirationDates -> UpDates-> UserSolicitud-> CounterStates

#Author
class Author(models.Model):
    name= models.CharField("Nombre", max_length=50)
    last_name = models.CharField("apellido", max_length=50) 
    image= models.ImageField("imagen", upload_to='bookflix/static/autores', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    description = models.TextField("descripcion",blank=True, null=True)
    created_date = models.DateTimeField("fecha de creacion", default=timezone.now)

    def publish(self):
        self.save()

    def ret(self):
        return self.name 

    def __str__(self):
        return "%s %s" % (self.name, self.last_name)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

#Gender
class Gender(models.Model):
    name= models.CharField("Nombre", max_length=50, unique=True)
    description = models.TextField("descripcion", blank=True, null=True)
    created_date = models.DateTimeField("fecha de creacion",default=timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"


#Editorial
class Editorial(models.Model):
    name= models.CharField("Nombre", max_length=50, primary_key=True)
    description = models.TextField("descripcion",blank=True, null=True)
    mail = models.EmailField( max_length=254, blank=True, null=True)
    created_date = models.DateTimeField("",default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Editoriales"    



class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')
        
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.is_active=True
        user.confirmo=True
        user.save(using=self.db)
        return user

    """ def get_by_natural_key(self, username):
       return self.get(username=username)"""

#ConfirmationMail
class ConfirmationMail(models.Model):
    mail= models.EmailField( max_length=254, unique=True)
    codigo = models.CharField( max_length=10)
    tipo = models.IntegerField()
    #tipo de mails de confirmacion: 1 para confirmar cuenta, 2 confirmar cambio de contraseña 

    def publish(self):
        self.save()
    def __str__(self):
        return self.email  
#Account
class Account(AbstractBaseUser):

    #Valores para los diferentes tipos de cuenta
    free='free'
    normal='normal'
    premium='premium'
    admin = 'admin'
    AC_CHOICES= (
        (free, 'free'),
        (normal, 'normal'),
        (premium, 'premium'),
        (admin, 'admin')
    )

    email = models.EmailField(verbose_name='mail',max_length=60, unique=True)
    username = models.CharField("nombre de usuario", max_length=50, unique=True)
    
    date_joined = models.DateTimeField(verbose_name='Fecha de creacion', auto_now_add=True)
    last_login = models.DateField(verbose_name='último logueo', auto_now=True)
    is_admin = models.BooleanField(default=False, verbose_name="es admin")
    is_active = models.BooleanField(default=True, verbose_name="está activo")
    is_staff = models.BooleanField(default=False, verbose_name="personal")
    is_superuser = models.BooleanField(default=False, verbose_name="super usuario")
    confirmo= models.BooleanField(default=False)
    plan = models.CharField( max_length=8, choices=AC_CHOICES, default=free)
    date_start_plan = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name="Fecha de inicio del plan")
    time_pay = models.IntegerField(default=0, verbose_name="Días pagados")
    objects = MyAccountManager()
    #tiempo = tiempo_restante()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def nombre(self):
        return self.username

    def tiempo_restante(self):
        tiempo_pagado = timedelta(days=self.time_pay)
        fecha_limite = tiempo_pagado + self.date_start_plan
        dias_restantes = fecha_limite - datetime.now().date()
        return dias_restantes.days

    def has_perm (self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"

    
#CreditCards
class CreditCards(models.Model):
    number = CardNumberField('numero')
    date_expiration= CardExpiryField('fecha de vencimiento')
    cod = SecurityCodeField('codigo de seguridad')
    card_name = models.CharField("nombre de tarjeta",max_length=50)
    bank = models.CharField(('banco'),max_length=50)
    user = models.OneToOneField(Account, on_delete=models.CASCADE,verbose_name="usuario")

    def publish(self):
        self.save()

    def __str__(self):
        return self.card_name

    class Meta:
        verbose_name = "Tarjeta"
        verbose_name_plural = "Tarjetas"



#CreditCardsUsed

class CreditCardsUsed(models.Model):
    number = CardNumberField('numero')
    date_expiration= CardExpiryField('fecha de vencimiento')
    cod = SecurityCodeField('codigo de seguridad')
    card_name = models.CharField("nombre de tarjeta",max_length=50)
    bank = models.CharField(('banco'),max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = "Tarjeta Usada"
        verbose_name_plural = "Tarjetas Usadas"

#Profile

class Profile(models.Model):
    name= models.CharField("nombre", max_length=50)
    account= models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="cuenta")
    is_active_now= models.BooleanField("esta activo ahora",default=False)
    hour_activation= models.DateTimeField("hora de activacion", auto_now=False, auto_now_add=False, blank=True, null=True)
    pleasures_gender = models.ManyToManyField(Gender, blank=True, null=True, verbose_name="genero")
    pleasures_author = models.ManyToManyField(Author, blank=True, null=True, verbose_name="autor")
    pleasures_editorial = models.ManyToManyField(Editorial,blank=True, null=True, verbose_name="editorial")
    
    date_of_creation = models.DateTimeField("fecha de creacion",default=timezone.now)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name  
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        unique_together= ('name', 'account')

def validateIsbnNum(value):
    if len(value) == 16 and value.isnumeric():
        return value
    else: 
        raise ValidationError('El isbn son 16 numeros')

def validateIsbnB(value):

    try:
        l= BookByChapter.objects.get(isbn= value)
        raise ValidationError(' isbn en uso por un libro de Capitulos')
    except BookByChapter.DoesNotExist:
        return value



"-------Book-------"
class Book(models.Model):
    isbn = models.CharField( max_length=16, unique=True, validators =[validateIsbnB, validateIsbnNum],)
    title = models.CharField(('titulo'), max_length=50)
    description = models.TextField(('descripcion'), blank=True, null=True)
    image= models.ImageField("imagen", upload_to='portadas_libros', height_field=None, width_field=None, max_length=None, )
    author= models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="autor")
    genders = models.ManyToManyField(Gender, verbose_name="generos")
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    mostrar_en_home= models.BooleanField(default=False)
    on_normal = models.BooleanField("ver en normal", default=False)
    on_premium = models.BooleanField("ver en premium",default=False)
    # pdf = models.FileField(upload_to='pdf', blank=True, null=True)   # cambiarlo para que guarde solo url?
    pdf = models.FileField(upload_to='pdf', blank=True, null=True)   #por si en un futuro hacemos que se guarde en la base de datos



    # veces_puntuado = models.FloatField(default=0,blank=True, null=True)
    # puntuacion = models.FloatField(default=0,blank=True, null=True)
    # puntuacion_acumulada = models.FloatField(default=0,blank=True, null=True)


    def publish(self):
    
        self.save()

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.title



def validateIsbn(value):

    try:
        l= Book.objects.get(isbn= value)
        raise ValidationError('isbn en uso por un libro')
    except Book.DoesNotExist:
        return value

 
"-------BookByChapter-------"
class BookByChapter(models.Model):
    isbn = models.CharField( max_length=16, unique=True, validators =[validateIsbn, validateIsbnNum], )
    title = models.CharField(('titulo'), max_length=50)
    cant_chapter = models.IntegerField('Cantidad de capitulos', default = 1)
    description = models.TextField(('descripcion'), blank=True, null=True)
    image= models.ImageField("imagen", upload_to='portadas_libros', height_field=None, width_field=None, max_length=None, )
    author= models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="autor")
    genders = models.ManyToManyField(Gender, verbose_name="generos")
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    mostrar_en_home= models.BooleanField(default=False)
    on_normal = models.BooleanField("ver en normal", default=False)
    on_premium = models.BooleanField("ver en premium",default=False)




    # veces_puntuado = models.IntegerField(default=0,blank=True, null=True)
    # puntuacion = models.FloatField(default=0,blank=True, null=True)
    # puntuacion_acumulada = models.FloatField(default=0,blank=True, null=True)

    def publish(self):
       
        self.save()

    def id(self):
        return self.id

    class Meta:
        verbose_name = "Libro por capítulo"
        verbose_name_plural = "Libro por capítulos"

    def __str__(self):
        return self.title



"-------LibroFavorito-------"
class LibroFavorito(models.Model):
    isbn = models.CharField( max_length=16, unique=True, validators =[validateIsbnB, validateIsbnNum],)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="perfil",blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="libro",blank=True, null=True)

    def publish(self):
        self.save()

    def id(self):
        return self.id

    class Meta:
        verbose_name = "Libro favorito"
        verbose_name_plural = "Libros favoritos"

    def __str__(self):
        return self.isbn


"-------LibroPorCapituloFavorito-------"
class LibroPorCapituloFavorito(models.Model):
    isbn = models.CharField( max_length=16, unique=True, validators =[validateIsbn, validateIsbnNum],)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="perfil",blank=True, null=True)
    book = models.ForeignKey(BookByChapter, on_delete=models.CASCADE, verbose_name="libro",blank=True, null=True)

    def publish(self):
        self.save()

    def id(self):
        return self.id

    class Meta:
        verbose_name = "Libro por capitulo favorito"
        verbose_name_plural = "Libros por capitulos favoritos"

    def __str__(self):
        return self.isbn




# "-------PuntuacionDeLibro-------"
# class PuntuacionDeLibro(models.Model):
#     isbn = models.CharField( max_length=16, validators =[validateIsbn, validateIsbnNum], )
#     title = models.CharField(('titulo'), max_length=50)
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="perfil")


    # def id(self):
    #         return self.id

    # def publish(self):
        
    #         self.save()

    # def __str__(self):
    #         return self.title

    # class Meta:
    #     verbose_name = "Puntuacion de libro"
    #     verbose_name_plural = "Puntuaciones de libros"


"-------Billboard-------"
class Billboard(models.Model):

    title = models.CharField("titulo", max_length=50 )
    description = models.TextField("descripcion",blank=True, null=True)
    mostrar_en_home= models.BooleanField(default=False)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="autor")
    video=  models.URLField(  max_length=255, blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"


"-------Trailer-------"
class Trailer(models.Model):
    title = models.CharField("titulo", max_length=50)
    description = models.TextField("descripcion",blank=True, null=True)
    mostrar_en_home= models.BooleanField(default=False)
    author = models.ForeignKey(Account, on_delete=models.CASCADE,verbose_name="autor")
    video=  models.URLField(  max_length=255, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="libro",blank=True, null=True)
    libro_por_capitulo = models.ForeignKey(BookByChapter, on_delete=models.CASCADE, verbose_name="libro por capitulo",blank=True, null=True)

    def publish(self):
        self.save()

    class Meta:
            verbose_name = "Trailer"
            verbose_name_plural = "Trailers"

    def __str__(self):
        return self.title

    def clean(self):
        if (self.book is None) and (self.libro_por_capitulo is None):
            raise ValidationError("Debe adjuntar un libro o libro por capitulo")
        if not (self.book is None) and  not (self.libro_por_capitulo is None):
            raise ValidationError("Debe adjuntar UN libro O UN libro por capitulo")
    

def numerolegal(value):
    if value == 0:
        raise ValidationError('un capitulo no puede ser numero cero')
    elif value < 0 :
        raise ValidationError('un capitulo no puede tener un numero negativo')
    else:
        return value

"-------Chapter-------"
class Chapter(models.Model):    
    book= models.ForeignKey(BookByChapter, on_delete=models.CASCADE, verbose_name="libro",) # validators=[libroLleno])
    title= models.CharField(("Titulo del capítulo"), max_length=50, help_text="Ingrese el nombre del capítulo, en caso de no tenerlo, su numero de cap, esta información se mostrará al usuario")
    number = models.IntegerField(("numero de capitulo"), validators=[numerolegal], help_text="este dato es solo para ordenar las busquedas internas, sepa que si un libro tiene dos capitulos y aquí pone 10 (en vez de 1) , no afectara al libro, pero en el orden se mostrara al final")
    description = models.TextField(("Descripción del capítulo"), blank=True, null=True)
    pdf = models.FileField(upload_to='pdf')
    active = models.BooleanField(("Activado"), default=False)

    class Meta:
        unique_together = ('number', 'book',)
        verbose_name = "Capítulo"
        verbose_name_plural = "Capítulos"

    def clean(self):
        b= BookByChapter.objects.get(id = self.book.id)
        b2= Chapter.objects.exclude(id= self.id).filter(book=self.book).count()
        if self.number > int(b.cant_chapter):
            raise ValidationError('no puede usar este numero para el capitulo')
        if b2 == b.cant_chapter:
            raise ValidationError('El libro no puede contener mas capítulos')
        if Chapter.objects.exclude(id=self.id).filter(book= self.book, number=self.number).exists():
            raise ValidationError('Ese numero de capítulo ya fue usado por ese capítulo')

    def publish(self):
        self.save()
        

    def __str__(self):
       
        return ' Libro: %s . Capitulo titulado: %s y es el capitulo numero: %s' % (self.book, self.title, self.number)

#StateOfBook

class StateOfBookByChapter(models.Model):

    reading='reading'
    future_reading='future_reading'
    finished='finished'
    AC_CHOICES= (
        (reading, 'leyendo'),
        (future_reading, 'futura lectura'),
        (finished, 'terminado')
    )

    date= models.DateField("fecha",default=timezone.now)
    state = models.CharField("estado", max_length=16, choices=AC_CHOICES, default=finished, blank=True, null=True)
    book = models.ForeignKey(BookByChapter, on_delete=models.CASCADE, verbose_name="libro")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="perfil")

    class Meta:
        unique_together= ('book', 'profile') 
        verbose_name = "Estado del libro por capítulo"
        verbose_name_plural = "Estados de libros por capítulo"
         
    def publish(self):
        self.save()

    def __str__(self):
        #b=BookByChapter.objects.get(isbn=self.book)
        return 'El libro %s del perfil: %s se encuentra en el estado: %s' % (self.book, self.profile.name, self.state)        

class StateOfBook(models.Model):

    reading='reading'
    future_reading='future_reading'
    finished='finished'
    AC_CHOICES= (
        (reading, 'leyendo'),
        (future_reading, 'futura lectura'),
        (finished, 'terminado')
    )

    date= models.DateField("fecha",default=timezone.now)
    state = models.CharField("estado", max_length=16, choices=AC_CHOICES, default=finished, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="libro")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="perfil")

    class Meta:
        unique_together= ('book', 'profile') 
        verbose_name = "Estado del libro"
        verbose_name_plural = "Estados del libro"
         
    def publish(self):
        self.save()

    def __str__(self):
        return 'El libro %s del perfil: %s se encuentra en el estado: %s' % (self.book, self.profile.name, self.state)      






"-------Capítulo Favorito-------"
class CapituloFavorito(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="perfil",blank=True, null=True)
    book = models.ForeignKey(BookByChapter, on_delete=models.CASCADE, verbose_name="libro",blank=True, null=True)
    titulo_capitulo = models.CharField(('titulo'), max_length=50)
    capitulo = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def id(self):
        return self.id

    class Meta:
        verbose_name = "Capitulo Favorito"
        verbose_name_plural = "Capitulos Favoritos"

    def __str__(self):
        return self.titulo_capitulo + "⠀del libro:⠀" +self.book.title 








# class StateOfBookGender(models.Model):

#     reading='reading'
#     future_reading='future_reading'
#     finished='finished'
#     AC_CHOICES= (
#         (reading, 'leyendo'),
#         (future_reading, 'futura lectura'),
#         (finished, 'terminado')
#     )

#     date= models.DateField("fecha",default=timezone.now)
#     state = models.CharField("estado", max_length=16, choices=AC_CHOICES, default=finished)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="libro")
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="perfil")

#     class Meta:
#         unique_together= ('book', 'profile') 
#         verbose_name = "Estado del libro"
#         verbose_name_plural = "Estados del libro"
         
#     def publish(self):
#         self.save()

#     def __str__(self):
#         return 'el libro %s se encuentra en el estado: %s' % (self.book, self.state)          









# class StateOfEditorial(models.Model):

#     reading='reading'
#     future_reading='future_reading'
#     finished='finished'
#     AC_CHOICES= (
#         (reading, 'leyendo'),
#         (future_reading, 'futura lectura'),
#         (finished, 'terminado')
#     )

#     date= models.DateField("fecha",default=timezone.now)
#     state = models.CharField("estado", max_length=16, choices=AC_CHOICES, default=finished)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="libro")
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="perfil")

#     class Meta:
#         unique_together= ('book', 'profile') 
#         verbose_name = "Estado del libro"
#         verbose_name_plural = "Estados del libro"
         
#     def publish(self):
#         self.save()

#     def __str__(self):
#         return 'el libro %s se encuentra en el estado: %s' % (self.book, self.state)          

















# class StateOfAuthor(models.Model):

#     reading='reading'
#     future_reading='future_reading'
#     finished='finished'
#     AC_CHOICES= (
#         (reading, 'leyendo'),
#         (future_reading, 'futura lectura'),
#         (finished, 'terminado')
#     )

#     date= models.DateField("fecha",default=timezone.now)
#     state = models.CharField("estado", max_length=16, choices=AC_CHOICES, default=finished)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="libro")
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="perfil")

#     class Meta:
#         unique_together= ('book', 'profile') 
#         verbose_name = "Estado del libro"
#         verbose_name_plural = "Estados del libro"
         
#     def publish(self):
#         self.save()

#     def __str__(self):
#         return 'el libro %s se encuentra en el estado: %s' % (self.book, self.state)          
















#Comment
class CommentBook(models.Model):

    is_a_spoiler = models.BooleanField("es espoiler",default=False)
    description = models.TextField("descripcion",)
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="perfil")
    publication = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="publicacion")
    #date = models.DateTimeField( default= datetime.now)   


    def publish(self):
        self.save()

    class Meta:
        verbose_name = "Comentario libro"
        verbose_name_plural = "Comentarios libros"

class CommentBookByChapter(models.Model):

    is_a_spoiler = models.BooleanField("es espoiler",default=False)
    description = models.TextField("descripcion",)
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="perfil")
    publication = models.ForeignKey(BookByChapter, on_delete=models.CASCADE, verbose_name="publicacion")    


    def publish(self):
        self.save()

    class Meta:
        verbose_name = "Comentario libro por capítulo"
        verbose_name_plural = "Comentarios libros por capítulo"    

#Like
class Like(models.Model):
    
    points = models.IntegerField("Puntos",default = False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="libro")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="autor")
    
    class Meta:
        unique_together = ('author', 'book')

    def publish(self):
        self.save()

    class Meta:
        verbose_name = "Me gusta libro"
        verbose_name_plural = "Me gusta/s libros"

class LikeBookByChapter(models.Model):
    
    points = models.IntegerField("Puntos",default = False)
    book = models.ForeignKey(BookByChapter, on_delete=models.CASCADE, verbose_name="libro")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="autor")
    
    class Meta:
        unique_together = ('author', 'book')

    def publish(self):
        self.save()

    class Meta:
        verbose_name = "Me gusta libro Por Capitulo"
        verbose_name_plural = "Me gusta/s libros por Capitulo"

#LikeComment
class LikeCommentBook(models.Model):
    
    is_like = models.BooleanField("me gusta",default = False)
    comment = models.ForeignKey(CommentBook, on_delete=models.CASCADE, verbose_name="comentario")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="autor")

    class Meta:
        unique_together = ('author', 'comment')
        verbose_name = "Me gusta de comentario"
        verbose_name_plural = "Me gustas/s de comentarios"

    def publish(self):
        self.save()

class LikeCommentBookByChapter(models.Model):
    
    is_like = models.BooleanField("me gusta",default = False)
    comment = models.ForeignKey(CommentBookByChapter, on_delete=models.CASCADE, verbose_name="comentario")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="autor")

    class Meta:
        unique_together = ('author', 'comment')
        verbose_name = "Me gusta de comentario"
        verbose_name_plural = "Me gustas/s de comentarios"

    def publish(self):
        self.save()

def esCorrecto(value):
    if datetime.now().date() >= value :
        raise ValidationError('La fecha no puede ser anterior a hoy. ni hoy')
    else:
        return value

class UpDownBook(models.Model):
    book = models.ForeignKey(Book, verbose_name=("libro"), on_delete=models.CASCADE)
    up_normal= models.DateField("pasar a normal", default= timezone.now(), validators=[esCorrecto])
    expiration_normal= models.DateField("expiracion normal", default= timezone.now(), validators=[esCorrecto])
    up_premium= models.DateField("pasar a premium",default= timezone.now(), validators=[esCorrecto])
    expiration_premium= models.DateField("expiracion premium", default= timezone.now(), validators=[esCorrecto])   

    def clean(self):
        if (self.up_normal >= self.expiration_normal):
            raise ValidationError('La fecha de baja no puede ser inferior a la de subida para normal o premium')
        if (self.up_premium >= self.expiration_premium):
            raise ValidationError('La fecha de baja no puede ser inferior a la de subida para premium o normal')

    class Meta:
        verbose_name = "Subir-Bajar-Libro"
        verbose_name_plural = "Subir-Bajar-Libro"

    def __str__(self):
        #boo= Book.objects.get(isbn=self.book)
        return str(self.book)
    
class UpDownBookByChapter(models.Model):
    book = models.ForeignKey(BookByChapter, verbose_name=("libro"), on_delete=models.CASCADE)
    up_normal= models.DateField("pasar a normal", default= timezone.now(), validators=[esCorrecto])
    expiration_normal= models.DateField("expiracion normal", default= timezone.now(), validators=[esCorrecto])
    up_premium= models.DateField("pasar a premium",default= timezone.now(), validators=[esCorrecto])
    expiration_premium= models.DateField("expiracion premium", default= timezone.now(), validators=[esCorrecto])    

    class Meta:
        verbose_name = "Subir-Bajar-LibroPorCapitulo"
        verbose_name_plural = "Subir-Bajar-LibroPorCapitulo"

    def clean(self):
        if (self.up_normal >= self.expiration_normal):
            raise ValidationError('La fecha de baja no puede ser inferior a la de subida para normal o premium')
        if (self.up_premium >= self.expiration_premium):
            raise ValidationError('La fecha de baja no puede ser inferior a la de subida para premium o normal')

    def __str__(self):
        str(self.book)
        return self.book.title
    
class UpDownChapter(models.Model):
    chapter = models.ForeignKey(Chapter, verbose_name=("Capitulo"), on_delete=models.CASCADE)
    up= models.DateField("DarDeAlta", default= timezone.now(), validators=[esCorrecto])
    expirationl= models.DateField("DarDeBaja", default= timezone.now(), validators=[esCorrecto])
    
    def clean(self):
        if (self.up >= self.expirationl):
            raise ValidationError('La fecha de baja no puede ser inferior a la de subida')
    
    class Meta:
        verbose_name = "Subir-Bajar-Capitulo"
        verbose_name_plural = "Subir-Bajar-Capitulos"

    def __str__(self):
        return str(self.chapter)
    

class UpDownBillboard(models.Model):
    Billboard = models.ForeignKey(Billboard, verbose_name=("Publicacion"), on_delete=models.CASCADE)
    up= models.DateField("DarDeAlta", default= timezone.now(), validators=[esCorrecto])
    expirationl= models.DateField("DarDeBaja", default= timezone.now(), validators=[esCorrecto])
    class Meta:
        verbose_name = "Subir-Bajar-Publicacion"
        verbose_name_plural = "Subir-Bajar-Publicaciones"

    def clean(self):
        if (self.up >= self.expirationl):
            raise ValidationError('La fecha de baja no puede ser inferior a la de subida')    

    def __str__(self):
        return str(self.Billboard)
    
class UpDownTrailer(models.Model):
    trailer = models.ForeignKey(Trailer, verbose_name=("Publicacion"), on_delete=models.CASCADE)
    up= models.DateField("DarDeAlta", default= timezone.now(), validators=[esCorrecto])
    expirationl= models.DateField("DarDeBaja", default= timezone.now(), validators=[esCorrecto])
    class Meta:
        verbose_name = "Subir-Bajar-Trailer"
        verbose_name_plural = "Subir-Bajar-Trailer"
    
    def clean(self):
        if (self.up >= self.expirationl):
            raise ValidationError('La fecha de baja no puede ser inferior a la de subida')

    def __str__(self):
        return str(self.trailer)
    

class UserSolicitud(models.Model):

    #tipo de solicitud tres valores: alta, baja, cambio
    type_of_solicitud = models.CharField("tipo de solicitud",  max_length=6)
    #Type_of_plan tres valores: free, normal, premium
    type_of_plan = models.CharField("tipo de plan", max_length=7)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name="usuario")
    date_of_solicitud = models.DateTimeField("fecha de solicitud",default=timezone.now)
    #Esta tendrá tres valores 0 sin tocar, 1 aceptada, 2 rechazada
    is_accepted= models.IntegerField(default=0, verbose_name="Fue aceptada")

    def publish(self):
        self.save()

    def __str__(self):
        return self.type_of_solicitud

    class Meta:
        verbose_name = "Solicitud de usuario"
        verbose_name_plural = "Solicitudes de Usuarios"

#CounterStates

class CounterStates(models.Model):

    publication = models.ForeignKey(Book, on_delete=models.CASCADE,verbose_name="publicacion") 
    date_start = models.DateField("fecha de inicio")                                                         
    cant_reading = models.IntegerField("leyendo",default=0)
    cant_future_read = models.IntegerField("en futuras lecturas",default=0)
    cant_finished = models.IntegerField("terminados",default=0)
    
    def publish(self):
        self.save()
    
    class Meta:
        verbose_name = "Estadística de libro"
        verbose_name_plural = "Estadísticas de libros"

class DenunciarComentarioLibro(models.Model):
    comentario = models.ForeignKey(CommentBook, on_delete=models.CASCADE)

class DenunciarComentarioLibroPorCap(models.Model):
    comentario = models.ForeignKey(CommentBookByChapter, on_delete=models.CASCADE)
    
    
class MailQueusoPrueba(models.Model):
    mail = models.EmailField( max_length=254, blank=True, null=True)


class TarjetaQueUsoPrueba(models.Model):
    numero = CardNumberField()


class CuentaqueUsoPrueba(models.Model):
    usuario = models.OneToOneField(Account, on_delete=models.CASCADE)
