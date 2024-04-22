# Generated by Django 5.0.4 on 2024-04-20 11:05

import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Foundation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=120)),
                ("sub_title", models.CharField(max_length=150)),
                ("description", models.TextField()),
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        upload_to="about_us/Foundation/image/", verbose_name="Image"
                    ),
                ),
            ],
            options={
                "verbose_name": "Foundation",
                "verbose_name_plural": "Histories",
                "db_table": "about_Foundation",
                "ordering": ("-id",),
            },
        ),
    ]
