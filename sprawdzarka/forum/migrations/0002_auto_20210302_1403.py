# Generated by Django 3.0.5 on 2021-03-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_content',
            field=models.CharField(default=None, max_length=256),
        ),
    ]