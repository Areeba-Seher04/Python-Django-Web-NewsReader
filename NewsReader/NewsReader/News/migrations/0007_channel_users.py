# Generated by Django 2.1.7 on 2019-04-14 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('News', '0006_auto_20190409_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='users',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
