# Generated by Django 3.1.2 on 2020-10-06 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoassign',
            old_name='todo',
            new_name='assign',
        ),
    ]
