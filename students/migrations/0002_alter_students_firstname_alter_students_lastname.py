# Generated by Django 4.1.2 on 2022-10-21 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='firstname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='students',
            name='lastname',
            field=models.TextField(max_length=200),
        ),
    ]
