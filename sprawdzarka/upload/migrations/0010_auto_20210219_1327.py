# Generated by Django 3.1.5 on 2021-02-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0009_auto_20210219_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plagiat',
            name='plagiat',
            field=models.IntegerField(),
        ),
    ]