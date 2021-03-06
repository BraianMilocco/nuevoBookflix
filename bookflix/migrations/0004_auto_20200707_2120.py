# Generated by Django 3.0.7 on 2020-07-08 00:20

import bookflix.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookflix', '0003_auto_20200707_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updownbillboard',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 265410, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updownbillboard',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 265382, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='expiration_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 262696, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion normal'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='expiration_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 262743, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion premium'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='up_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 262653, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a normal'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='up_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 262719, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a premium'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='expiration_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 263767, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion normal'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='expiration_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 263835, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion premium'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='up_normal',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 263722, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a normal'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='up_premium',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 263796, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a premium'),
        ),
        migrations.AlterField(
            model_name='updownchapter',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 264739, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updownchapter',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 264709, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
        migrations.AlterField(
            model_name='updowntrailer',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 266065, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updowntrailer',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 7, 8, 0, 20, 4, 266036, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
    ]
