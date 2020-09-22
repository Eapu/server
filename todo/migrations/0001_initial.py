# Generated by Django 3.1.1 on 2020-09-22 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=50)),
                ('author', models.TextField(blank=True, max_length=50)),
                ('content', models.TextField(blank=True, max_length=50)),
            ],
        ),
    ]
