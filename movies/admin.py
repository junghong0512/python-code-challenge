from django.contrib import admin
from . import models


@admin.register(models.Actor)
class ItemAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    """ Custom Movie Admin """

    list_filter = (
        "director",
        "category",
        "rating",
        "country",
    )

    list_display = (
        "title",
        "year",
        "country",
        "director",
        "rating",
    )