# Generated by Django 2.0 on 2021-04-09 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(default='Enter Email', max_length=25, unique=True)),
                ('Password', models.CharField(default='Enter Password', max_length=25)),
                ('Role', models.CharField(default='Enter Role', max_length=25)),
                ('Otp', models.IntegerField(default=123456)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='Firstname', max_length=100)),
                ('Lastname', models.CharField(default='Lasttname', max_length=100)),
                ('Address', models.CharField(default='Address', max_length=255)),
                ('Age', models.IntegerField(null=True)),
                ('PhoneNumber', models.IntegerField(null=True)),
                ('Gender', models.CharField(default='Gender', max_length=100)),
                ('Department', models.CharField(max_length=80, null=True)),
                ('ProfilePic', models.ImageField(default='abc', upload_to='')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='Firstname', max_length=100)),
                ('Lastname', models.CharField(default='Lasttname', max_length=100)),
                ('Address', models.CharField(default='Address', max_length=255)),
                ('Age', models.IntegerField(default=0)),
                ('PhoneNumber', models.IntegerField(default=1234567890)),
                ('Gender', models.CharField(default='Gender', max_length=100)),
                ('ProfilePic', models.ImageField(default='abc', upload_to='')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Admin')),
            ],
        ),
    ]
