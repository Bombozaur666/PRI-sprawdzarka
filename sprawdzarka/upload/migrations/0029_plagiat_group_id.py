# Generated by Django 3.1.7 on 2021-03-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0028_auto_20210306_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='plagiat',
            name='group_id',
            field=models.IntegerField(default=-1),
        ),
    ]
