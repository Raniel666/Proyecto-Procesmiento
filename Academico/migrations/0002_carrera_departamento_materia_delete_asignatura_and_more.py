# Generated by Django 4.1.7 on 2023-02-28 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('codigo_c', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('costo', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('codigo_dep', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('carrera_ids', models.ManyToManyField(related_name='Carreras', to='Academico.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('codigo', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('creditos', models.PositiveIntegerField()),
                ('creditos_requerido', models.IntegerField()),
                ('abierta', models.BooleanField(default=True)),
                ('carrera', models.CharField(choices=[('Industrial', 'Ingieneria Industrial'), ('Mecanica', 'Ingieneria Mecanica'), ('Sistemas', 'Ingieneria Sistemas'), ('General', 'General')], max_length=15, verbose_name='Carrera')),
                ('departamento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academico.departamento')),
            ],
        ),
        migrations.DeleteModel(
            name='Asignatura',
        ),
        migrations.AddField(
            model_name='usuario',
            name='carrera_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Academico.carrera'),
        ),
    ]
