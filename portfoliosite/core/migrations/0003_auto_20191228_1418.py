# Generated by Django 3.0.1 on 2019-12-28 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191228_0418'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
        migrations.RenameModel(
            old_name='CompletedProjects',
            new_name='CompletedProject',
        ),
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
    ]
