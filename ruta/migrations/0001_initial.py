# Generated by Django 4.1.7 on 2023-03-06 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departamento",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "nombre",
                    models.CharField(max_length=20, verbose_name="Departamento"),
                ),
            ],
            options={
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Ruta",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=40, verbose_name="Ruta")),
            ],
            options={
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Municipio",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=30, verbose_name="Municipio")),
                (
                    "departamento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ruta.departamento",
                    ),
                ),
            ],
            options={
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="CentroAcopio",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "nombre",
                    models.CharField(max_length=40, verbose_name="Centro de Acopio"),
                ),
                (
                    "municipio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ruta.municipio"
                    ),
                ),
            ],
            options={
                "verbose_name": "Centro de Acopio",
                "verbose_name_plural": "Centros de Acopio",
                "ordering": ["pk"],
            },
        ),
    ]