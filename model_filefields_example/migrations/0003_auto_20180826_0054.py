# Generated by Django 2.1 on 2018-08-26 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_filefields_example', '0002_auto_20180826_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcover',
            name='bytes',
            field=models.BinaryField(),
        ),
    ]
