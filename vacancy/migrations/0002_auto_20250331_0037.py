# Generated by Django 3.2.3 on 2025-03-30 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacancy.description'),
        ),
    ]
