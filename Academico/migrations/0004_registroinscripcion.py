# Generated by Django 4.1.6 on 2023-03-01 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0003_materia_semestre'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroInscripcion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_apertura', models.DateTimeField()),
                ('fecha_inscripcion', models.DateTimeField()),
                ('estado', models.CharField(choices=[('inscribiendo', 'Inscribiendo'), ('pago', 'Pago'), ('inscrito', 'Inscrito')], max_length=15)),
                ('estudiante_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('materias_ids', models.ManyToManyField(to='Academico.materia')),
            ],
        ),
    ]
