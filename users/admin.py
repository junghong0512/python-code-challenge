from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "bio",
                    "preference",
                    "language",
                    "favorite_book_genre",
                    "favorite_movie_genre",
                ),
            },
        ),
    )
    list_filter = (
        "preference",
        "language",
        "favorite_book_genre",
        "favorite_movie_genre",
    )
