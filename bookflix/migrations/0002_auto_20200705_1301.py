# Generated by Django 3.0.7 on 2020-07-05 16:01

import bookflix.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookflix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updownbillboard',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 406862, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updownbillboard',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 406829, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='expiration_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 404486, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion normal'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='expiration_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 404533, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion premium'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='up_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 404448, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a normal'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='up_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 404510, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a premium'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='expiration_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 405278, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion normal'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='expiration_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 405325, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion premium'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='up_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 405245, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a normal'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='up_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 405302, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a premium'),
        ),
        migrations.AlterField(
            model_name='updownchapter',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 406058, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updownchapter',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 406026, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
        migrations.AlterField(
            model_name='updowntrailer',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 407767, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updowntrailer',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 7, 5, 16, 1, 58, 407733, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
    ]
