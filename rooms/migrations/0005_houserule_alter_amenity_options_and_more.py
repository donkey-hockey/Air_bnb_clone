# Generated by Django 4.1b1 on 2022-07-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0004_amenity_facility_houserull_remove_room_room_type_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HouseRule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("update", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=40)),
            ],
            options={
                "verbose_name": "House Rule",
            },
        ),
        migrations.AlterModelOptions(
            name="amenity",
            options={"verbose_name_plural": "Amenities"},
        ),
        migrations.AlterModelOptions(
            name="facility",
            options={"verbose_name_plural": "Facilities"},
        ),
        migrations.AlterModelOptions(
            name="roomtype",
            options={"verbose_name": "Room Type"},
        ),
        migrations.RemoveField(
            model_name="room",
            name="house_rulls",
        ),
        migrations.AddField(
            model_name="amenity",
            name="name",
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name="facility",
            name="name",
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name="roomtype",
            name="name",
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.DeleteModel(
            name="HouseRull",
        ),
        migrations.AddField(
            model_name="room",
            name="house_rules",
            field=models.ManyToManyField(to="rooms.houserule"),
        ),
    ]
