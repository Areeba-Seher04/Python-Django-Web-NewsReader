# Generated by Django 2.1.7 on 2019-04-17 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0020_auto_20190417_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chan',
            old_name='albums',
            new_name='album',
        ),
    ]
