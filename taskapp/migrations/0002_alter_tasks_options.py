# Generated by Django 3.2.7 on 2021-09-05 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['-pk'], 'verbose_name_plural': 'Task Manager'},
        ),
    ]
