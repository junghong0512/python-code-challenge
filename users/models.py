from django.contrib.auth.models import AbstractUser
from django.db import models
from categories import models as category_models


class User(AbstractUser):

    """ Custom User Model """

    PREFERENCE_BOOKS = "books"
    PREFERENCE_MOVIES = "movies"

    PREFERENCE_CHOICES = (
        (PREFERENCE_BOOKS, "Books"),
        (PREFERENCE_MOVIES, "Movies"),
    )

    LANGUAGE_KOREAN = "kr"
    LANGUAGE_ENGLISH = "en"

    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_ENGLISH, "English"),
    )

    bio = models.TextField(default="", blank=True)
    preference = models.CharField(
        choices=PREFERENCE_CHOICES, max_length=200, blank=True
    )
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    fav_book_genre = models.ForeignKey(
        category_models.Category,
        related_name="favorite_book_genre",
        on_delete=models.CASCADE,
        null=True,
    )
    fav_movie_genre = models.ForeignKey(
        category_models.Category,
        related_name="favorite_movie_genre",
        on_delete=models.CASCADE,
        null=True,
    )
