# Generated by Django 5.0.2 on 2024-02-25 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="nickname",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone",
        ),
    ]
