# Generated by Django 3.1.7 on 2021-03-03 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0019_auto_20210225_1315'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Promela',
        ),
        migrations.DeleteModel(
            name='Promela2',
        ),
        migrations.DeleteModel(
            name='TaskListPromela',
        ),
    ]