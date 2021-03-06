# Generated by Django 3.1 on 2021-11-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addvehicle',
            fields=[
                ('Sr', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=250)),
                ('route', models.CharField(default='', max_length=300)),
                ('speed', models.CharField(default='', max_length=200)),
                ('avgspeed', models.CharField(default='', max_length=200)),
                ('engstatus', models.CharField(default='', max_length=500)),
                ('fuel', models.IntegerField(default=0)),
                ('temp', models.CharField(default='', max_length=200)),
                ('staticmap', models.ImageField(upload_to='addvehicle/')),
            ],
        ),
    ]
