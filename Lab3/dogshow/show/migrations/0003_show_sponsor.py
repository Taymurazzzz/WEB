# Generated by Django 5.1.3 on 2025-02-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0002_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='sponsor',
            field=models.ManyToManyField(to='show.sponsor'),
        ),
    ]
