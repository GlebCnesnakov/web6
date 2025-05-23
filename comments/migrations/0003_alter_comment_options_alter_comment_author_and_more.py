# Generated by Django 5.1.6 on 2025-04-27 14:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комменатрии'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(choices=[(False, 'Не опубликовано'), (True, 'Опубликовано')], default=1, verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='текст'),
        ),
    ]
