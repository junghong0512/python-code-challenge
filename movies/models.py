from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
from categories import models as category_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Actor(AbstractItem):

    pass


class Movie(core_models.TimeStampedModel):

    """ Movie Model Definition """

    title = models.CharField(max_length=50)
    cover_image = models.ImageField(blank=True)
    year = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    country = CountryField()
    desciption = models.TextField()
    director = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor, blank=True)
    category = models.ManyToManyField(category_models.Category, blank=True)
    rating = models.IntegerField(blank=True)

    def __str__(self):
        return self.title
