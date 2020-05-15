# Generated by Django 3.0.6 on 2020-05-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookflix', 'C:\\Users\\Julian\\Desktop\\ProyectosDjango\\nuevo0002_auto_20200514_0302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Cuenta', 'verbose_name_plural': 'Cuentas'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
        migrations.AlterModelOptions(
            name='creditcards',
            options={'verbose_name': 'Tarjeta', 'verbose_name_plural': 'Tarjetas'},
        ),
        migrations.AlterModelOptions(
            name='gender',
            options={'verbose_name': 'Genero', 'verbose_name_plural': 'Generos'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfiles'},
        ),
        migrations.AddField(
            model_name='profile',
            name='hour_activation',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]