# Generated by Django 4.2.6 on 2023-11-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]