# Generated by Django 2.2.4 on 2019-08-15 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PyCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('street', models.CharField(max_length=100)),
                ('street_2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('rut', models.CharField(max_length=12)),
                ('giro', models.CharField(max_length=80)),
            ],
        ),
    ]
