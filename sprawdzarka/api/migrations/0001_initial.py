# Generated by Django 3.1.1 on 2020-09-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('snumber', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]