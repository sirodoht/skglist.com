# Generated by Django 2.1 on 2018-08-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("votes", models.PositiveIntegerField()),
                ("link", models.URLField()),
                ("is_eat", models.BooleanField()),
                ("is_drink", models.BooleanField()),
            ],
        )
    ]
