# Generated by Django 3.0.8 on 2020-09-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date', 'time']},
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(verbose_name='military time'),
        ),
    ]
