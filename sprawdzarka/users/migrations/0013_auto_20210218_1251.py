# Generated by Django 3.1.5 on 2021-02-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210218_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='group',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]
