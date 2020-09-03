from django.db import models
from core import models as core_models


class Category(core_models.TimeStampedModel):

    """ Category Model Definition """

    name = models.CharField(max_length=30)
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name
