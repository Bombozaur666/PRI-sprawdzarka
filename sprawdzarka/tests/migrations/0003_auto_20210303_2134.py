# Generated by Django 3.1.7 on 2021-03-03 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210303_2134'),
        ('tests', '0002_auto_20210303_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testfilemodel',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.group', verbose_name='Grupa'),
        ),
    ]