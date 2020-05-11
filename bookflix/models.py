from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

from django.utils import timezone

#Probando, va a quedar un choclo gigante con todos los objetos aca
#Orden Author-> Gender-> Editorial-> CreditCards-> Account-> Profile->  
# Publication (y sus hijos)-> StateOfBook-> Comment -> Like -> LikeComment -->>
# -> ExpirationDates -> UpDates-> UserSolicitud-> CounterStates

#Author
class Author(models.Model):
    name= models.CharField("Nombre", max_length=50)
    last_name = models.CharField( max_length=50) 
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)


    def publish(self):
        self.save()

    def ret(sel):
        return self.name 
    def __str__(self):
        return self.name

#Gender
class Gender(models.Model):
    name= models.CharField("Nombre", max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

#Editorial
class Editorial(models.Model):
    name= models.CharField("Nombre", max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    mail = models.EmailField( max_length=254, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

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
        user.save(using=self.db)
        return user



#Account
class Account(AbstractBaseUser):

    #Valores para los diferentes tipos de cuenta
    free='1'
    normal='2'
    premium='4'
    admin = '9'
    AC_CHOICES= (
        (free, 'free'),
        (normal, 'normal'),
        (premium, 'premium'),
        (admin, 'admin')
    )

    email = models.EmailField(verbose_name='email address',max_length=60, unique=True)
    username = models.CharField( max_length=50, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    plan = models.CharField( max_length=2, choices=AC_CHOICES, default=free)
    date_start_plan = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    time_pay = models.IntegerField(default=0)
    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm (self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    
#CreditCards
class CreditCards(models.Model):
    number = models.CharField(max_length=16, primary_key=True)
    cod = models.IntegerField()
    card_name = models.CharField(max_length=50)
    date_expiration = models.DateField(auto_now=False, auto_now_add=False)
    bank = models.CharField(max_length=50)
    user = models.OneToOneField(Account, on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return self.card_name

#Profile

class Profile(models.Model):
    account= models.ForeignKey(Account, on_delete=models.CASCADE)
    name= models.CharField( max_length=50)
    pleasures_gender = models.ManyToManyField(Gender, blank=True, null=True)
    pleasures_author = models.ManyToManyField(Author, blank=True, null=True)
    pleasures_editorial = models.ManyToManyField(Editorial,blank=True, null=True)
    
    date_of_creation = models.DateTimeField(default=timezone.now)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name  

      


"""Se guardan la clase publicación y sus hijos, libro, libro por capítulo, billboard, chapter """

"-------Publication-------"
class Publication(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField()
    on_normal = models.BooleanField(default=False)
    on_premium = models.BooleanField(default=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

"-------Book-------"
class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    author= models.ForeignKey(Author, on_delete=models.CASCADE)
    genders = models.ManyToManyField(Gender)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    url = models.URLField( max_length=200, blank=True, null=True)
    publication= models.OneToOneField(Publication, on_delete=models.CASCADE)

    def publish(self):
        self.save()

 
"-------BookByChapter-------"
class BookByChapter(models.Model):
    book= models.OneToOneField(Book, on_delete=models.CASCADE)
    cant_chapter = models.IntegerField(default = 1)
    
    def publish(self):
        self.save()


"-------Billboard-------"
class Billboard(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    video=  models.URLField(   max_length=255, blank=True, null=True)

    def publish(self):
        self.save()

"-------Chapter-------"
class Chapter(models.Model):
    number = models.IntegerField(default=0)
    book= models.ForeignKey(BookByChapter, on_delete=models.CASCADE)
    url = models.URLField( max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ('number', 'book',)

    def publish(self):
        self.save()

#StateOfBook

class StateOfBook(models.Model):

    reading='10'
    future_reading='20'
    finished='30'
    AC_CHOICES= (
        (reading, 'reading'),
        (future_reading, 'future_reading'),
        (finished, 'finished')
    )

    date= models.DateField(default=timezone.now)
    state = models.CharField( max_length=2, choices=AC_CHOICES, default=finished)
    book = models.ForeignKey(Publication, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together= ('book', 'profile') 
         
    def publish(self):
        self.save()

    def __str__(self):
        return self.state        

#Comment
class Comment(models.Model):

    is_a_spoiler = models.BooleanField(default=False)
    description = models.TextField()
    profile= models.ForeignKey(Profile, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)    


    def publish(self):
        self.save()

#Like
class Like(models.Model):
    
    is_like = models.BooleanField(default = False)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('author', 'publication')

    def publish(self):
        self.save()



#LikeComment
class LikeComment(models.Model):
    
    is_like = models.BooleanField(default = False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('author', 'comment')

    def publish(self):
        self.save()

#ExpirationDates
class ExpirationDates(models.Model):

    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    expiration_normal= models.DateField(blank=True, null=True)
    expiration_premium= models.DateField(blank=True, null=True)

    def publish(self):
        self.save()

#UpDates
class   UpDates(models.Model):
    
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    up_normal= models.DateField(blank=True, null=True)
    up_premium= models.DateField(blank=True, null=True)

    def publish(self):
        self.save()


#UserSolicitud

class UserSolicitud(models.Model):
    pass
    "Valores para los diferentes tipos de cuenta"
    alta='1'
    cambio='2'
    baja='4'
    AC_CHOICES= (
        (alta, 'alta'),
        (cambio, 'cambio'),
        (baja, 'baja')
    )
    free = 'f'
    normal = 'n'
    premium = 'p'
    TY_CHOICES= (
        (free, 'free'),
        (normal, 'normal'),
        (premium, 'premium')
    )
    "Valores del modelo"    
    """Si se pide una baja, se debe llenar con la fecha en que termina el plan.
        Si se pude el cambio, apenas empieza el dia de que termine el tiempo pagado del usuario,
        se debería cambiar el usuario al plan nuevo """

    """en caso de que el usuario quiera pagar tiempo hay que revisar que no tenga una solicitud de
      cambio de plan, en ese caso se debe generar una solicitud de alta con el plan nuevo y el tiempo"""  

    "tipo de solicitud que se hace"
    type_of_solicitud = models.CharField( max_length=2, choices=AC_CHOICES, default=alta)
    "tipo de plan al que se quiere cambiar, en caso de que sea baja, por defecto es free"
    type_of_plan = models.CharField( max_length=2, choices=TY_CHOICES, default=free)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_of_solicitud = models.DateTimeField(default=timezone.now)
    "fecha limite para atender la solicitud, si es un alta es un dia despues de la fecha de creacion"
    "si es un cambio o baja es cuando se termina el tiempo comprado por el usuario"
    date_limit_to_attend = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.type_of_solicitud

#CounterStates

class CounterStates(models.Model):

    publication = models.ForeignKey(Publication, on_delete=models.CASCADE) 
    date_start = models.DateField( )
    date_start = models.DateField( )
    cant_reading = models.IntegerField(default=0)
    cant_future_read = models.IntegerField(default=0)
    cant_finished = models.IntegerField(default=0)

    
    def publish(self):
        self.save()