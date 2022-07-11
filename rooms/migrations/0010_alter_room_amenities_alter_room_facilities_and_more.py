# Generated by Django 4.1b1 on 2022-07-11 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0009_alter_photo_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="amenities",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="rooms.amenity"
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="facilities",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="rooms.facility"
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="house_rules",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="rooms.houserule"
            ),
        ),
    ]
