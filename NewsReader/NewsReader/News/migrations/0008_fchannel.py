# Generated by Django 2.1.7 on 2019-04-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0007_channel_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='FChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_logo', models.FileField(upload_to='')),
                ('src', models.CharField(default='', max_length=250)),
            ],
        ),
    ]