# Generated by Django 4.0.6 on 2022-07-09 12:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_banaulasmodeli_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='banaulasmodeli',
            name='mesaj',
            field=models.TextField(default=datetime.datetime(2022, 7, 9, 12, 18, 0, 338833, tzinfo=utc)),
            preserve_default=False,
        ),
    ]