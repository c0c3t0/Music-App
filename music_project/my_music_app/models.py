from django.core.validators import MinLengthValidator
from django.db import models

from music_project.my_music_app.validators import username_validator, positive_num_validator


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            username_validator,
        ),
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LEN = 30
    ARTIST_NAME_MAX_LEN = 30
    GENRE_NAME_MAX_LEN = 30

    POP = 'Pop Music'
    JAZZ = 'Jazz Music'
    RB = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIP_HOP = "Hip Hop Music"
    OTHER = "Other"

    GENRES = [(x, x) for x in (POP, JAZZ, RB, ROCK, COUNTRY, DANCE, HIP_HOP, OTHER)]

    album_name = models.CharField(
        max_length=ALBUM_NAME_MAX_LEN,
        unique=True,
    )

    artist = models.CharField(
        max_length=ALBUM_NAME_MAX_LEN,
    )

    genre = models.CharField(
        max_length=GENRE_NAME_MAX_LEN,
        choices=GENRES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            positive_num_validator,
        ),
    )