# Generated by Django 3.0.7 on 2020-06-21 18:28

import bookflix.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookflix', '0003_auto_20200622_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updownbillboard',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 526102, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updownbillboard',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 526064, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='expiration_normal',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 523672, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion normal'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='expiration_premium',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 523721, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion premium'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='up_normal',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 523633, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a normal'),
        ),
        migrations.AlterField(
            model_name='updownbook',
            name='up_premium',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 523697, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a premium'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='expiration_normal',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 524479, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion normal'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='expiration_premium',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 524527, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='expiracion premium'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='up_normal',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 524448, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a normal'),
        ),
        migrations.AlterField(
            model_name='updownbookbychapter',
            name='up_premium',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 524503, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='pasar a premium'),
        ),
        migrations.AlterField(
            model_name='updownchapter',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 525275, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updownchapter',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 525243, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
        migrations.AlterField(
            model_name='updowntrailer',
            name='expirationl',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 527054, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeBaja'),
        ),
        migrations.AlterField(
            model_name='updowntrailer',
            name='up',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 18, 28, 3, 527020, tzinfo=utc), validators=[bookflix.models.esCorrecto], verbose_name='DarDeAlta'),
        ),
    ]
