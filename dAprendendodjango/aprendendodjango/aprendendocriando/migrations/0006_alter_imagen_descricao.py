# Generated by Django 5.1.6 on 2025-02-23 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aprendendocriando', '0005_imagen_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='descricao',
            field=models.CharField(max_length=500000, null=True),
        ),
    ]
