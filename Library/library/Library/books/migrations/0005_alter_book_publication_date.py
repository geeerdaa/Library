# Generated by Django 4.2.4 on 2023-08-14 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0004_delete_createbook"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="publication_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 8, 14, 18, 41, 33, 87659, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
