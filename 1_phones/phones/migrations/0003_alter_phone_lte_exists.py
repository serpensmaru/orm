# Generated by Django 4.1 on 2022-08-05 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_rename_lte_exist_phone_lte_exists_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(),
        ),
    ]
