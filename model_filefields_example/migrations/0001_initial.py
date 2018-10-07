# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_pk', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('index', models.FileField(blank=True, null=True, upload_to=b'model_filefields_example.BookIndex/bytes/filename/mimetype')),
                ('pages', models.FileField(blank=True, null=True, upload_to=b'model_filefields_example.BookPages/bytes/filename/mimetype')),
                ('cover', models.ImageField(blank=True, null=True, upload_to=b'model_filefields_example.BookCover/bytes/filename/mimetype')),
            ],
        ),
        migrations.CreateModel(
            name='BookCover',
            fields=[
                ('book_cover_pk', models.AutoField(primary_key=True, serialize=False)),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=255)),
                ('mimetype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookIndex',
            fields=[
                ('book_index_pk', models.AutoField(primary_key=True, serialize=False)),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=255)),
                ('mimetype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookPages',
            fields=[
                ('book_pages_pk', models.AutoField(primary_key=True, serialize=False)),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=255)),
                ('mimetype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SoundDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('instruction_manual', models.FileField(blank=True, null=True, upload_to=b'model_filefields_example.SoundDeviceInstructionManual/bytes/filename/mimetype')),
            ],
        ),
        migrations.CreateModel(
            name='SoundDeviceInstructionManual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=255)),
                ('mimetype', models.CharField(max_length=50)),
            ],
        ),
    ]