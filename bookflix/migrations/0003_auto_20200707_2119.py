# Generated by Django 3.0.7 on 2020-07-08 00:19

import bookflix.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookflix', '0002_auto_20200706_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updownbillboard',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 543848, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updownbillboard',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 543798, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='expiration_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 540732, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion normal'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='expiration_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 540793, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion premium'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='up_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 540686, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a normal'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='up_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 540762, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a premium'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='expiration_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 541775, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion normal'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='expiration_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 541848, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion premium'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='up_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 541735, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a normal'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='up_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 541807, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a premium'),
        ),
        migrations.AlterField(
            model_name='updownchapter',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 542891, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updownchapter',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 542850, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
        migrations.AlterField(
            model_name='updowntrailer',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 545160, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updowntrailer',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 19, 34, 545106, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
    ]