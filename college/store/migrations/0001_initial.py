# Generated by Django 4.1.5 on 2023-04-18 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('DOB', models.DateField()),
                ('Age', models.IntegerField()),
                ('Gender', models.TextField()),
                ('Phone', models.IntegerField()),
                ('Email', models.TextField()),
                ('Address', models.TextField()),
                ('Department', models.TextField()),
                ('Material', models.TextField()),
            ],
        ),
    ]
