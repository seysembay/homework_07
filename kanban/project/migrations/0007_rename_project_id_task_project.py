# Generated by Django 4.2.2 on 2023-06-28 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_rename_project_task_project_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='project_id',
            new_name='project',
        ),
    ]
