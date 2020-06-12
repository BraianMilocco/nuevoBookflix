# Generated by Django 3.0.6 on 2020-06-11 23:54

import bookflix.models
import creditcards.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='mail')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='nombre de usuario')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('confirmo', models.BooleanField(default=False)),
                ('plan', models.CharField(choices=[('free', 'free'), ('normal', 'normal'), ('premium', 'premium'), ('admin', 'admin')], default='free', max_length=8)),
                ('date_start_plan', models.DateField(blank=True, null=True)),
                ('time_pay', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='apellido')),
                ('image', models.ImageField(blank=True, null=True, upload_to='bookflix/static/autores', verbose_name='imagen')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha de creacion')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Billboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='titulo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('mostrar_en_home', models.BooleanField(default=False)),
                ('video', models.URLField(blank=True, max_length=255, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autor')),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=16, primary_key=True, serialize=False, validators=[bookflix.models.validateIsbnB, bookflix.models.validateIsbnNum])),
                ('title', models.CharField(max_length=50, verbose_name='titulo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='portadas_libros', verbose_name='imagen')),
                ('mostrar_en_home', models.BooleanField(default=False)),
                ('on_normal', models.BooleanField(default=False, verbose_name='ver en normal')),
                ('on_premium', models.BooleanField(default=False, verbose_name='ver en premium')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Author', verbose_name='autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
        migrations.CreateModel(
            name='BookByChapter',
            fields=[
                ('isbn', models.CharField(max_length=16, primary_key=True, serialize=False, validators=[bookflix.models.validateIsbn, bookflix.models.validateIsbnNum])),
                ('title', models.CharField(max_length=50, verbose_name='titulo')),
                ('cant_chapter', models.IntegerField(default=1, verbose_name='Cantidad de capitulos')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='portadas_libros', verbose_name='imagen')),
                ('mostrar_en_home', models.BooleanField(default=False)),
                ('on_normal', models.BooleanField(default=False, verbose_name='ver en normal')),
                ('on_premium', models.BooleanField(default=False, verbose_name='ver en premium')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Author', verbose_name='autor')),
            ],
            options={
                'verbose_name': 'Libro por capítulo',
                'verbose_name_plural': 'Libro por capítulos',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Ingrese el nombre del capítulo, en caso de no tenerlo, su numero de cap, esta información se mostrará al usuario', max_length=50, validators=[bookflix.models.numerolegal], verbose_name='Titulo del capítulo')),
                ('number', models.IntegerField(help_text='este dato es solo para ordenar las busquedas internas, sepa que si un libro tiene dos capitulos y aquí pone 10 (en vez de 1) , no afectara al libro, pero en el orden se mostrara al final', verbose_name='numero de capitulo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción del capítulo')),
                ('pdf', models.FileField(upload_to='pdf')),
                ('active', models.BooleanField(default=False, verbose_name='Activado')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.BookByChapter', validators=[bookflix.models.libroLleno], verbose_name='libro')),
            ],
            options={
                'verbose_name': 'Capítulo',
                'verbose_name_plural': 'Capítulos',
                'unique_together': {('number', 'book')},
            },
        ),
        migrations.CreateModel(
            name='CommentBookByChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_spoiler', models.BooleanField(default=False, verbose_name='es espoiler')),
                ('description', models.TextField(verbose_name='descripcion')),
            ],
            options={
                'verbose_name': 'Comentario libro por capítulo',
                'verbose_name_plural': 'Comentarios libros por capítulo',
            },
        ),
        migrations.CreateModel(
            name='ConfirmationMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('codigo', models.CharField(max_length=10)),
                ('tipo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='')),
            ],
            options={
                'verbose_name_plural': 'Editoriales',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha de creacion')),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
                ('is_active_now', models.BooleanField(default=False, verbose_name='esta activo ahora')),
                ('hour_activation', models.DateTimeField(blank=True, null=True, verbose_name='hora de activacion')),
                ('date_of_creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha de creacion')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='cuenta')),
                ('pleasures_author', models.ManyToManyField(blank=True, null=True, to='bookflix.Author', verbose_name='autor')),
                ('pleasures_editorial', models.ManyToManyField(blank=True, null=True, to='bookflix.Editorial', verbose_name='editorial')),
                ('pleasures_gender', models.ManyToManyField(blank=True, null=True, to='bookflix.Gender', verbose_name='genero')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='titulo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('mostrar_en_home', models.BooleanField(default=False)),
                ('video', models.URLField(blank=True, max_length=255, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autor')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Book', verbose_name='libro')),
            ],
            options={
                'verbose_name': 'Trailer',
                'verbose_name_plural': 'Trailers',
            },
        ),
        migrations.CreateModel(
            name='UserSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_solicitud', models.CharField(choices=[('1', 'alta'), ('2', 'cambio'), ('4', 'baja')], default='1', max_length=2, verbose_name='tipo de solicitud')),
                ('type_of_plan', models.CharField(choices=[('f', 'free'), ('n', 'normal'), ('p', 'premium')], default='f', max_length=2, verbose_name='tipo de plan')),
                ('date_of_solicitud', models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha de solicitud')),
                ('date_limit_to_attend', models.DateTimeField(blank=True, null=True, verbose_name='fecha limite')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'Solicitud de usuario',
                'verbose_name_plural': 'Solicitudes de Usuarios',
            },
        ),
        migrations.CreateModel(
            name='UpDownTrailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 804057, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta')),
                ('expirationl', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 804057, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja')),
                ('trailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Trailer', verbose_name='Publicacion')),
            ],
            options={
                'verbose_name': 'Subir-Bajar-Trailer',
                'verbose_name_plural': 'Subir-Bajar-Trailer',
            },
        ),
        migrations.CreateModel(
            name='UpDownChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 803058, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta')),
                ('expirationl', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 803058, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Chapter', verbose_name='Capitulo')),
            ],
            options={
                'verbose_name': 'Subir-Bajar-Capitulo',
                'verbose_name_plural': 'Subir-Bajar-Capitulos',
            },
        ),
        migrations.CreateModel(
            name='UpDownBookByChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_normal', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 802057, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a normal')),
                ('expiration_normal', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 802057, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion normal')),
                ('up_premium', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 802057, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a premium')),
                ('expiration_premium', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 802057, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion premium')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.BookByChapter', verbose_name='libro')),
            ],
            options={
                'verbose_name': 'Subir-Bajar-LibroPorCapitulo',
                'verbose_name_plural': 'Subir-Bajar-LibroPorCapitulo',
            },
        ),
        migrations.CreateModel(
            name='UpDownBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_normal', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 802057, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a normal')),
                ('expiration_normal', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 802057, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion normal')),
                ('up_premium', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 802057, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a premium')),
                ('expiration_premium', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 802057, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion premium')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Book', verbose_name='libro')),
            ],
            options={
                'verbose_name': 'Subir-Bajar-Libro',
                'verbose_name_plural': 'Subir-Bajar-Libro',
            },
        ),
        migrations.CreateModel(
            name='UpDownBillboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 803058, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta')),
                ('expirationl', models.DateField(default=datetime.datetime(2020, 6, 11, 23, 54, 57, 804057, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja')),
                ('Billboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Billboard', verbose_name='Publicacion')),
            ],
            options={
                'verbose_name': 'Subir-Bajar-Publicacion',
                'verbose_name_plural': 'Subir-Bajar-Publicaciones',
            },
        ),
        migrations.CreateModel(
            name='LikeBookByChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=False, verbose_name='me gusta')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile', verbose_name='autor')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.BookByChapter', verbose_name='libro')),
            ],
            options={
                'verbose_name': 'Me gusta libro Por Capitulo',
                'verbose_name_plural': 'Me gusta/s libros por Capitulo',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=False, verbose_name='me gusta')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile', verbose_name='autor')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Book', verbose_name='libro')),
            ],
            options={
                'verbose_name': 'Me gusta libro',
                'verbose_name_plural': 'Me gusta/s libros',
            },
        ),
        migrations.CreateModel(
            name='DenunciarComentarioLibro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.CommentBookByChapter')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', creditcards.models.CardNumberField(max_length=25, verbose_name='numero')),
                ('date_expiration', creditcards.models.CardExpiryField(verbose_name='fecha de vencimiento')),
                ('cod', creditcards.models.SecurityCodeField(max_length=4, verbose_name='codigo de seguridad')),
                ('card_name', models.CharField(max_length=50, verbose_name='nombre de tarjeta')),
                ('bank', models.CharField(max_length=50, verbose_name='banco')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'Tarjeta',
                'verbose_name_plural': 'Tarjetas',
            },
        ),
        migrations.CreateModel(
            name='CounterStates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(verbose_name='fecha de inicio')),
                ('cant_reading', models.IntegerField(default=0, verbose_name='leyendo')),
                ('cant_future_read', models.IntegerField(default=0, verbose_name='en futuras lecturas')),
                ('cant_finished', models.IntegerField(default=0, verbose_name='terminados')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Book', verbose_name='publicacion')),
            ],
            options={
                'verbose_name': 'Estadística de libro',
                'verbose_name_plural': 'Estadísticas de libros',
            },
        ),
        migrations.AddField(
            model_name='commentbookbychapter',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile', verbose_name='perfil'),
        ),
        migrations.AddField(
            model_name='commentbookbychapter',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.BookByChapter', verbose_name='publicacion'),
        ),
        migrations.CreateModel(
            name='CommentBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_spoiler', models.BooleanField(default=False, verbose_name='es espoiler')),
                ('description', models.TextField(verbose_name='descripcion')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile', verbose_name='perfil')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Book', verbose_name='publicacion')),
            ],
            options={
                'verbose_name': 'Comentario libro',
                'verbose_name_plural': 'Comentarios libros',
            },
        ),
        migrations.AddField(
            model_name='bookbychapter',
            name='editorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Editorial'),
        ),
        migrations.AddField(
            model_name='bookbychapter',
            name='genders',
            field=models.ManyToManyField(to='bookflix.Gender', verbose_name='generos'),
        ),
        migrations.AddField(
            model_name='book',
            name='editorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Editorial'),
        ),
        migrations.AddField(
            model_name='book',
            name='genders',
            field=models.ManyToManyField(to='bookflix.Gender', verbose_name='generos'),
        ),
        migrations.CreateModel(
            name='StateOfBookByChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='fecha')),
                ('state', models.CharField(choices=[('reading', 'leyendo'), ('future_reading', 'futura lectura'), ('finished', 'terminado')], default='finished', max_length=16, verbose_name='estado')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.BookByChapter', verbose_name='libro')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile', verbose_name='perfil')),
            ],
            options={
                'verbose_name': 'Estado del libro por capítulo',
                'verbose_name_plural': 'Estados de libros por capítulo',
                'unique_together': {('book', 'profile')},
            },
        ),
        migrations.CreateModel(
            name='StateOfBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='fecha')),
                ('state', models.CharField(choices=[('reading', 'leyendo'), ('future_reading', 'futura lectura'), ('finished', 'terminado')], default='finished', max_length=16, verbose_name='estado')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Book', verbose_name='libro')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile', verbose_name='perfil')),
            ],
            options={
                'verbose_name': 'Estado del libro',
                'verbose_name_plural': 'Estados del libro',
                'unique_together': {('book', 'profile')},
            },
        ),
        migrations.CreateModel(
            name='LikeCommentBookByChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=False, verbose_name='me gusta')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile', verbose_name='autor')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.CommentBookByChapter', verbose_name='comentario')),
            ],
            options={
                'verbose_name': 'Me gusta de comentario',
                'verbose_name_plural': 'Me gustas/s de comentarios',
                'unique_together': {('author', 'comment')},
            },
        ),
        migrations.CreateModel(
            name='LikeCommentBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=False, verbose_name='me gusta')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile', verbose_name='autor')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.CommentBook', verbose_name='comentario')),
            ],
            options={
                'verbose_name': 'Me gusta de comentario',
                'verbose_name_plural': 'Me gustas/s de comentarios',
                'unique_together': {('author', 'comment')},
            },
        ),
    ]
