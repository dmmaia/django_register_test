# Generated by Django 3.2.12 on 2023-06-30 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app__register_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
