# Generated by Django 2.0 on 2021-04-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210409_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='Loc',
            field=models.CharField(default='location', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='Loc',
            field=models.CharField(default='location', max_length=50),
        ),
    ]