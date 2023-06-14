# Generated by Django 4.2.2 on 2023-06-13 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0001_initial'),
        ('tasks', '0005_alter_tasks_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='task_stage', to='stage.stagetasks'),
        ),
    ]
