# Generated by Django 4.2.2 on 2023-06-28 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='user_id',
            new_name='user',
        ),
    ]
