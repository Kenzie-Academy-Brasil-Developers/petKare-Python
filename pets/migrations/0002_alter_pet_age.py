# Generated by Django 4.1.3 on 2022-12-01 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="age",
            field=models.IntegerField(),
        ),
    ]
