# Generated by Django 4.1.2 on 2022-10-29 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='namse',
        ),
    ]
