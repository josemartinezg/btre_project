# Generated by Django 2.1.7 on 2019-04-08 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_emergencia', models.CharField(max_length=200)),
                ('antecedentes_patologicos', models.TextField(blank=True)),
                ('antecedentes_hereditarios', models.TextField(blank=True)),
                ('antecedentes_alergicos', models.TextField(blank=True)),
                ('estado_tratamiento', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.Usuario')),
                ('deleted', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
