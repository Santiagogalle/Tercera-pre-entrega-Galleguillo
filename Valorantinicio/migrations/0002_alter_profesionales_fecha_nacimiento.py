# Generated by Django 4.2.2 on 2023-06-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Valorantinicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesionales',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]