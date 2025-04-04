# Generated by Django 5.1.6 on 2025-02-12 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.category'),
        ),
    ]
