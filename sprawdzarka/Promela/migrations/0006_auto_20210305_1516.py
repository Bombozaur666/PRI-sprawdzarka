# Generated by Django 3.0.5 on 2021-03-05 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Promela', '0005_auto_20210305_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttask',
            name='output_file',
            field=models.FileField(upload_to='', verbose_name='Output'),
        ),
    ]