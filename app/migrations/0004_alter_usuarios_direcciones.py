# Generated by Django 4.2.5 on 2023-12-17 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_paquetes_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='direcciones',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.direcciones'),
        ),
    ]
