# Generated by Django 2.1.7 on 2019-04-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.URLField(max_length=10000),
        ),
    ]
