# Generated by Django 3.1.1 on 2020-09-01 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_preference'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_book_genre',
            field=models.CharField(blank=True, choices=[('adventure', 'Adventure'), ('classics', 'Classics'), ('comic', 'Comic'), ('detective', 'Detective'), ('fantasy', 'Fantasy'), ('history', 'History'), ('horror', 'Horror'), ('literacy', 'Literacy'), ('romance', 'Romance'), ('science', 'Science'), ('short', 'Short Stories'), ('suspence', 'Suspence'), ('thriller', 'Thriller'), ('biography', 'Biography'), ('essay', 'Essay'), ('memoir', 'Memoir'), ('poetry', 'Poetry'), ('selfhelp', 'Self Help'), ('others', 'Others')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('kr', 'Korean'), ('en', 'English')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='preference',
            field=models.CharField(blank=True, choices=[('books', 'Books'), ('movies', 'Movies')], max_length=20, null=True),
        ),
    ]