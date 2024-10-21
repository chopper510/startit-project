# Generated by Django 5.1.2 on 2024-10-16 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'Афиша', 'verbose_name_plural': 'Афиши'},
        ),
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(max_length=100, verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(verbose_name='Описание афиши'),
        ),
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название афиши'),
        ),
    ]