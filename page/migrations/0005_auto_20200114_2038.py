# Generated by Django 3.0.2 on 2020-01-14 20:38

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('page', '0004_auto_20200114_1958'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]