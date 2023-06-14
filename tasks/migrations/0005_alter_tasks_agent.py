# Generated by Django 4.2.2 on 2023-06-13 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_alter_agent_celular_alter_agent_cnpj_alter_agent_cpf_and_more'),
        ('tasks', '0004_alter_tasks_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='agent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='agent', to='agent.agent'),
        ),
    ]
