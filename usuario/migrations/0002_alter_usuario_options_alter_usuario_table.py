# Generated by Django 5.0.4 on 2024-05-02 21:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("usuario", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="usuario",
            options={},
        ),
        migrations.AlterModelTable(
            name="usuario",
            table="auth_user",
        ),
    ]
