# Generated by Django 2.0 on 2021-04-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_bookartistreq'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookartistreq',
            name='Status',
            field=models.CharField(default='Status', max_length=100),
        ),
    ]
