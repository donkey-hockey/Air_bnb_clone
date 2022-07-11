# Generated by Django 4.1b1 on 2022-07-10 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("rooms", "0007_alter_room_amenities_alter_room_facilities_and_more"),
        ("reservations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="geust",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reservations",
                to="rooms.room",
            ),
        ),
    ]
