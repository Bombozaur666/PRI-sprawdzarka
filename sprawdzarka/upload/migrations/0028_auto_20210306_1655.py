# Generated by Django 3.1.7 on 2021-03-06 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0027_tasklist_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendedtasks',
            name='taskid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.tasklist'),
        ),
    ]
