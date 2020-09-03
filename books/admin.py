from django.contrib import admin
from . import models


@admin.register(models.Author)
class ItemAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    """ Custom Book Admin """

    list_filter = (
        "rating",
        "country",
        "author",
    )

    list_display = (
        "title",
        "year",
        "country",
        "rating",
    )