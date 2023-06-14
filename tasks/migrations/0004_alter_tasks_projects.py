# Generated by Django 4.2.2 on 2023-06-12 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projects_description'),
        ('tasks', '0003_tasks_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='projects',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='task_project', to='projects.projects'),
        ),
    ]