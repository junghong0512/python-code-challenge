from django.contrib.auth.models import AbstractUser
from django.db import models


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

    BOOK_GENRE_ADVENTURE = "adventure"
    BOOK_GENRE_CLASSIC = "classics"
    BOOK_GENRE_COMIC = "comic"
    BOOK_GENRE_DETECTIVE = "detective"
    BOOK_GENRE_FANTASY = "fantasy"
    BOOK_GENRE_HISTORY = "history"
    BOOK_GENRE_HORROR = "horror"
    BOOK_GENRE_LITERACY = "literacy"
    BOOK_GENRE_ROMANCE = "romance"
    BOOK_GENRE_SCIENCE = "science"
    BOOK_GENRE_SHORT_STORIES = "short"
    BOOK_GENRE_SUSPENCE = "suspence"
    BOOK_GENRE_THRILLER = "thriller"
    BOOK_GENRE_BIOGRAPHY = "biography"
    BOOK_GENRE_ESSAY = "essay"
    BOOK_GENRE_MEMOIR = "memoir"
    BOOK_GENRE_POETRY = "poetry"
    BOOK_GENRE_SELFHELP = "selfhelp"
    BOOK_GENRE_OTHERS = "others"

    BOOK_GENRE_CHOICES = (
        (BOOK_GENRE_ADVENTURE, "Adventure"),
        (BOOK_GENRE_CLASSIC, "Classics"),
        (BOOK_GENRE_COMIC, "Comic"),
        (BOOK_GENRE_DETECTIVE, "Detective"),
        (BOOK_GENRE_FANTASY, "Fantasy"),
        (BOOK_GENRE_HISTORY, "History"),
        (BOOK_GENRE_HORROR, "Horror"),
        (BOOK_GENRE_LITERACY, "Literacy"),
        (BOOK_GENRE_ROMANCE, "Romance"),
        (BOOK_GENRE_SCIENCE, "Science"),
        (BOOK_GENRE_SHORT_STORIES, "Short Stories"),
        (BOOK_GENRE_SUSPENCE, "Suspence"),
        (BOOK_GENRE_THRILLER, "Thriller"),
        (BOOK_GENRE_BIOGRAPHY, "Biography"),
        (BOOK_GENRE_ESSAY, "Essay"),
        (BOOK_GENRE_MEMOIR, "Memoir"),
        (BOOK_GENRE_POETRY, "Poetry"),
        (BOOK_GENRE_SELFHELP, "Self Help"),
        (BOOK_GENRE_OTHERS, "Others"),
    )

    MOVIE_GENRE_ADVENTURE = "adventure"
    MOVIE_GENRE_ANIMATION = "animation"
    MOVIE_GENRE_COMEDY = "comedy"
    MOVIE_GENRE_CRIME = "crime"
    MOVIE_GENRE_DRAMA = "drama"
    MOVIE_GENRE_FANTASY = "fantasy"
    MOVIE_GENRE_HISTORY = "history"
    MOVIE_GENRE_HORROR = "horror"
    MOVIE_GENRE_MYSTERY = "mystery"
    MOVIE_GENRE_PHILOSOPHICAL = "philosophical"
    MOVIE_GENRE_POLITICAL = "political"
    MOVIE_GENRE_ROMANCE = "romance"
    MOVIE_GENRE_SAGA = "saga"
    MOVIE_GENRE_SCIENCE = "science"
    MOVIE_GENRE_SPECULATIVE = "speculative"
    MOVIE_GENRE_THRILLER = "thriller"
    MOVIE_GENRE_URBAN = "urban"

    MOVIE_GENRE_CHOICES = (
        (MOVIE_GENRE_ADVENTURE, "Adventure"),
        (MOVIE_GENRE_ANIMATION, "Animation"),
        (MOVIE_GENRE_COMEDY, "Comedy"),
        (MOVIE_GENRE_CRIME, "Crime"),
        (MOVIE_GENRE_DRAMA, "Drama"),
        (MOVIE_GENRE_FANTASY, "Fantasy"),
        (MOVIE_GENRE_HISTORY, "History"),
        (MOVIE_GENRE_HORROR, "Horror"),
        (MOVIE_GENRE_MYSTERY, "Mystery"),
        (MOVIE_GENRE_PHILOSOPHICAL, "Philosophical"),
        (MOVIE_GENRE_POLITICAL, "Political"),
        (MOVIE_GENRE_ROMANCE, "Romance"),
        (MOVIE_GENRE_SAGA, "Saga"),
        (MOVIE_GENRE_SCIENCE, "Science"),
        (MOVIE_GENRE_SPECULATIVE, "Speculative"),
        (MOVIE_GENRE_THRILLER, "Thriller"),
        (MOVIE_GENRE_URBAN, "Urban"),
    )

    bio = models.TextField(default="", blank=True)
    preference = models.CharField(choices=PREFERENCE_CHOICES, max_length=20, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    favorite_book_genre = models.CharField(
        choices=BOOK_GENRE_CHOICES, max_length=20, blank=True
    )
    favorite_movie_genre = models.CharField(
        choices=MOVIE_GENRE_CHOICES, max_length=20, blank=True
    )
