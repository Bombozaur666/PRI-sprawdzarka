# Generated by Django 3.1.7 on 2021-03-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_studentanswermodel_is_right'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentanswermodel',
            old_name='task_id',
            new_name='question_id',
        ),
        migrations.AddField(
            model_name='studentanswermodel',
            name='test_id',
            field=models.IntegerField(default=0),
        ),
    ]
