# Generated by Django 4.2.5 on 2023-12-03 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquetes',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='paquetes',
            name='peso',
        ),
        migrations.RemoveField(
            model_name='paquetes',
            name='remitente',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
