# Generated by Django 2.0 on 2021-04-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210409_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='PhoneNumber',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Age',
            field=models.BigIntegerField(default=0),
        ),
    ]