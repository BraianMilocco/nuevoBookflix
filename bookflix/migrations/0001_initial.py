# Generated by Django 3.0.6 on 2020-05-10 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
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
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('plan', models.CharField(choices=[('1', 'free'), ('2', 'normal'), ('4', 'premium'), ('9', 'admin')], default='1', max_length=2)),
                ('date_start_plan', models.DateField(blank=True, null=True)),
                ('time_pay', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Author')),
            ],
        ),
        migrations.CreateModel(
            name='BookByChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_chapter', models.IntegerField(default=1)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_of_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pleasures_author', models.ManyToManyField(blank=True, null=True, to='bookflix.Author')),
                ('pleasures_editorial', models.ManyToManyField(blank=True, null=True, to='bookflix.Editorial')),
                ('pleasures_gender', models.ManyToManyField(blank=True, null=True, to='bookflix.Gender')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('on_normal', models.BooleanField(default=False)),
                ('on_premium', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_solicitud', models.CharField(choices=[('1', 'alta'), ('2', 'cambio'), ('4', 'baja')], default='1', max_length=2)),
                ('type_of_plan', models.CharField(choices=[('f', 'free'), ('n', 'normal'), ('p', 'premium')], default='f', max_length=2)),
                ('date_of_solicitud', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_limit_to_attend', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UpDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_normal', models.DateField(blank=True, null=True)),
                ('up_premium', models.DateField(blank=True, null=True)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Publication')),
            ],
        ),
        migrations.CreateModel(
            name='ExpirationDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_normal', models.DateField(blank=True, null=True)),
                ('expiration_premium', models.DateField(blank=True, null=True)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Publication')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCards',
            fields=[
                ('number', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('cod', models.IntegerField()),
                ('card_name', models.CharField(max_length=50)),
                ('date_expiration', models.DateField()),
                ('bank', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CounterStates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('cant_reading', models.IntegerField(default=0)),
                ('cant_future_read', models.IntegerField(default=0)),
                ('cant_finished', models.IntegerField(default=0)),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Publication')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_spoiler', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Publication')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='editorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Editorial'),
        ),
        migrations.AddField(
            model_name='book',
            name='genders',
            field=models.ManyToManyField(to='bookflix.Gender'),
        ),
        migrations.AddField(
            model_name='book',
            name='publication',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Publication'),
        ),
        migrations.CreateModel(
            name='Billboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField(blank=True, max_length=255, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StateOfBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('state', models.CharField(choices=[('10', 'reading'), ('20', 'future_reading'), ('30', 'finished')], default='30', max_length=2)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Publication')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile')),
            ],
            options={
                'unique_together': {('book', 'profile')},
            },
        ),
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Comment')),
            ],
            options={
                'unique_together': {('author', 'comment')},
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Profile')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.Publication')),
            ],
            options={
                'unique_together': {('author', 'publication')},
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('url', models.URLField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookflix.BookByChapter')),
            ],
            options={
                'unique_together': {('number', 'book')},
            },
        ),
    ]