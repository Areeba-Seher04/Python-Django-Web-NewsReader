# Generated by Django 2.1.7 on 2019-04-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0008_fchannel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fchannel',
            name='channel_logo',
        ),
        migrations.AddField(
            model_name='fchannel',
            name='channel_title',
            field=models.CharField(default=True, max_length=250),
        ),
    ]
