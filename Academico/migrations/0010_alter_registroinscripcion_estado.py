# Generated by Django 4.1.6 on 2023-03-02 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0009_alter_registroinscripcion_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroinscripcion',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('pago', 'Estado pagando'), ('inscrito', 'Inscrito')], default='pendiente', max_length=15),
        ),
    ]
