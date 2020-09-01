# Generated by Django 3.1.1 on 2020-09-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200902_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_movie_genre',
            field=models.CharField(blank=True, choices=[('adventure', 'Adventure'), ('animation', 'Animation'), ('comedy', 'Comedy'), ('crime', 'Crime'), ('drama', 'Drama'), ('fantasy', 'Fantasy'), ('history', 'History'), ('horror', 'Horror'), ('mystery', 'Mystery'), ('philosophical', 'Philosophical'), ('political', 'Political'), ('romance', 'Romance'), ('saga', 'Saga'), ('science', 'Science'), ('speculative', 'Speculative'), ('thriller', 'Thriller'), ('urban', 'Urban')], max_length=20, null=True),
        ),
    ]
