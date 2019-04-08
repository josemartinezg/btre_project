# Generated by Django 2.1.7 on 2019-04-08 00:50

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_usuario', models.CharField(choices=[('PA', 'Paciente'), ('EM', 'Empleado')], max_length=3)),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('primer_nombre', models.CharField(max_length=50)),
                ('segundo_nombre', models.CharField(blank=True, max_length=50)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(blank=True, max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('cedula', models.CharField(default='000-0000000-0', max_length=13)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1)),
                ('grupo_sanguineo', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=4)),
                ('linea_direccion_1', models.CharField(max_length=120)),
                ('linea_direccion_2', models.CharField(blank=True, max_length=120)),
                ('sector', models.CharField(max_length=120)),
                ('ciudad', models.CharField(max_length=120)),
                ('pais', django_countries.fields.CountryField(max_length=2)),
                ('nacionalidad', models.CharField(choices=[('RD', 'Dominicano'), ('HT', 'Haitiano'), ('USA', 'Estadounidense'), ('CU', 'Cubano')], max_length=75)),
                ('nss', models.CharField(max_length=13)),
                ('foto_perfil', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('deleted', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
