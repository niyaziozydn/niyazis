# Generated by Django 4.0.6 on 2022-07-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_sorumodeli_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorumodeli',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]