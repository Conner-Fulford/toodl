# Generated by Django 4.2.6 on 2023-11-07 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_alter_event_description_alter_event_endtime_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
