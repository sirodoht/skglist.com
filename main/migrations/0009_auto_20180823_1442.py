# Generated by Django 2.1 on 2018-08-23 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("main", "0008_auto_20180823_1441")]

    operations = [
        migrations.AlterField(
            model_name="vote",
            name="place",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="main.Place"
            ),
            preserve_default=False,
        )
    ]
