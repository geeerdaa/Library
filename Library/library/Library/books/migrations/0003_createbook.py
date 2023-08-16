# Generated by Django 4.2.4 on 2023-08-14 10:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_alter_book_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="CreateBook",
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
                ("title", models.CharField(max_length=50)),
                ("author", models.CharField(max_length=100)),
            ],
        ),
    ]