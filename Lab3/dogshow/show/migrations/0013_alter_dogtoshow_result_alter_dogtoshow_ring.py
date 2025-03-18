# Generated by Django 5.1.7 on 2025-03-18 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("show", "0012_alter_dogtoshow_result_alter_dogtoshow_ring"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dogtoshow",
            name="result",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="show.exercise",
            ),
        ),
        migrations.AlterField(
            model_name="dogtoshow",
            name="ring",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="show.ring",
            ),
        ),
    ]
