# Generated by Django 3.0.5 on 2021-03-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Promela', '0003_auto_20210304_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttask',
            name='has_been_tested',
            field=models.BooleanField(default=False),
        ),
    ]