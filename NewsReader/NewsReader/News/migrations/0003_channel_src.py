# Generated by Django 2.1.7 on 2019-04-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_auto_20190407_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='src',
            field=models.CharField(default='', max_length=250),
        ),
    ]
