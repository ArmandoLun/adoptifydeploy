# Generated by Django 3.0 on 2020-09-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMascotas', '0003_publicacion_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='report',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1),
        ),
    ]
