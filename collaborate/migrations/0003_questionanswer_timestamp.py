# Generated by Django 2.0.5 on 2019-04-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborate', '0002_askquestion_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionanswer',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]