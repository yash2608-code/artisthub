# Generated by Django 2.0 on 2021-04-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210413_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='tagline',
        ),
        migrations.AddField(
            model_name='artist',
            name='Designation',
            field=models.CharField(default='Who You Are', max_length=100),
        ),
    ]
