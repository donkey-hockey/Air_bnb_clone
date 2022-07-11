from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """User Model Definition"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
    )

    LANGUAGE_EN = "english"
    LANGUAGE_KR = "korean"
    LANGUAGE_CHOICES = (
        (LANGUAGE_EN, "English"),
        (LANGUAGE_KR, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = (
        (CURRENCY_USD, "usd"),
        (CURRENCY_KRW, "krw"),
    )

    avatar = models.ImageField(blank=True, upload_to="avatars")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=7, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)

    superhost = models.BooleanField(default=False)
