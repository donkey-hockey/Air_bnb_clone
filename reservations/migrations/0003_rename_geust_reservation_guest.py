# Generated by Django 4.1b1 on 2022-07-10 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reservations", "0002_alter_reservation_geust_alter_reservation_room"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reservation",
            old_name="geust",
            new_name="guest",
        ),
    ]
