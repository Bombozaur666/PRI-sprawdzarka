# Generated by Django 3.1.7 on 2021-03-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_auto_20210304_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPoitsTest',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('snumber', models.CharField(max_length=6)),
                ('test_id', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
    ]
