# Generated by Django 4.1 on 2022-08-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_alter_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
