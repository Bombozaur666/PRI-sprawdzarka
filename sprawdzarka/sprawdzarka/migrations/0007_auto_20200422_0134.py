# Generated by Django 3.0.5 on 2020-04-22 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200422_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendedtasks',
            name='task',
            field=models.FileField(upload_to='task/SendedTasks/'),
        ),
    ]
