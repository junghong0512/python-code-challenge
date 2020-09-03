from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
from categories import models as category_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Author(AbstractItem):

    pass


class Book(core_models.TimeStampedModel):

    """ Movie Model Definition """

    title = models.CharField(max_length=50)
    cover_image = models.ImageField(blank=True)
    year = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    country = CountryField()
    desciption = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(category_models.Category, blank=True)
    rating = models.IntegerField(blank=True)

    def __str__(self):
        return self.title
