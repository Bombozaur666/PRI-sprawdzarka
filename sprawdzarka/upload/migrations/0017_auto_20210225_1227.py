# Generated by Django 3.1.7 on 2021-02-25 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0016_auto_20210225_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sendedtasks',
            options={'ordering': ('group', 'taskid')},
        ),
    ]