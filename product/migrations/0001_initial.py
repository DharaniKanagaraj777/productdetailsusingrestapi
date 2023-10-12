# Generated by Django 4.2.4 on 2023-10-08 08:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductDetail",
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
                ("customername", models.CharField(max_length=30)),
                ("productname", models.CharField(max_length=30)),
                ("quantity", models.IntegerField()),
                ("address", models.CharField(max_length=20)),
            ],
        ),
    ]