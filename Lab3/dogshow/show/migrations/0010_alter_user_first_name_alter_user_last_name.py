# Generated by Django 5.1.7 on 2025-03-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("show", "0009_alter_user_email_alter_user_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(verbose_name="first name"),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(verbose_name="last name"),
        ),
    ]
