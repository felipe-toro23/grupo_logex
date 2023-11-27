# Generated by Django 4.2.5 on 2023-11-27 10:05

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id_cuenta', models.AutoField(primary_key=True, serialize=False)),
                ('rut_cli', models.CharField(max_length=12, unique=True)),
                ('nombre_cli', models.CharField(max_length=25)),
                ('apellido_cli', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('comuna', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle_dire', models.CharField(max_length=100)),
                ('numeracio_dire', models.IntegerField()),
                ('detalle_recep', models.CharField(blank=True, max_length=400, null=True)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to='app.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Paquetes',
            fields=[
                ('id_paquete', models.AutoField(primary_key=True, serialize=False)),
                ('nom_paq', models.CharField(max_length=50)),
                ('nom_recep', models.CharField(max_length=50)),
                ('cel_recep', models.BigIntegerField()),
                ('peso', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('fec_reti', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('detalles_paq', models.CharField(blank=True, max_length=300, null=True)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paquetes', to=settings.AUTH_USER_MODEL)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paquetes_direccion', to='app.direcciones')),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paquetes_remitidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlanillasEntregas',
            fields=[
                ('id_entregas', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fech_entrega', models.DateField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entregas', to='app.paquetes')),
            ],
        ),
        migrations.CreateModel(
            name='PlanillaRetiros',
            fields=[
                ('id_reti', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retiros', to='app.paquetes')),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retiros_remitidos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usuarios',
            name='direcciones',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.direcciones'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='usuarios_set_custom', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='usuarios_set_custom', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
