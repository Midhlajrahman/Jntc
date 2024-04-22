# Generated by Django 5.0.4 on 2024-04-22 09:55

import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("about", "0007_ptacommitee"),
    ]

    operations = [
        migrations.CreateModel(
            name="Commitee",
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
                ("name", models.CharField(max_length=120)),
                (
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        upload_to="about_us/commitee/images/", verbose_name="Image"
                    ),
                ),
                ("designation", models.CharField(max_length=120)),
                ("is_deleted", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Our Commitee",
                "verbose_name_plural": "Our Commitees",
                "db_table": "about_our_commitee",
                "ordering": ("id",),
            },
        ),
    ]
