# Generated by Django 3.0.7 on 2020-06-22 02:43

import bookflix.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookflix', '0005_auto_20200622_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updownbillboard',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 495359, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updownbillboard',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 495325, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='expiration_normal',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 492997, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion normal'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='expiration_premium',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 493047, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion premium'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='up_normal',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 492957, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a normal'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='up_premium',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 493022, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a premium'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='expiration_normal',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 493833, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion normal'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='expiration_premium',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 493881, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion premium'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='up_normal',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 493801, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a normal'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='up_premium',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 493857, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a premium'),
        ),
        migrations.AlterField(
            model_name='updownchapter',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 494617, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updownchapter',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 494586, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
        migrations.AlterField(
            model_name='updowntrailer',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 496256, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updowntrailer',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 6, 22, 2, 43, 30, 496222, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
    ]
