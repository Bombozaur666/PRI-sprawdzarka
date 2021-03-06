# Generated by Django 3.1.7 on 2021-03-06 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210305_1728'),
        ('Promela', '0008_studenttask_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttask',
            name='group_id',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='teachertask',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.group'),
        ),
    ]
