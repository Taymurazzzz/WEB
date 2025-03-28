# Generated by Django 5.1.3 on 2025-01-17 13:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelservice', '0003_alter_reservation_visitor_alter_review_user_nick_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='room_id',
            new_name='room',
        ),
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
