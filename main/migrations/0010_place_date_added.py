# Generated by Django 2.1 on 2018-08-26 12:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("main", "0009_auto_20180823_1442")]

    operations = [
        migrations.AddField(
            model_name="place",
            name="date_added",
            field=models.DateTimeField(default=django.utils.timezone.now),
        )
    ]