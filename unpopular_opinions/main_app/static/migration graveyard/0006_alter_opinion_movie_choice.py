# Generated by Django 4.2.2 on 2023-06-20 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_opinion_movie_choice_alter_opinion_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='movie_choice',
            field=models.CharField(choices=[('Select Movie', 'Select Movie'), (2, 'It'), (1, 'Interstellar'), (9, 'Minority Report'), (10, 'Arrival'), (12, 'Tron'), (13, 'Tron: Legacy')], default=('Select Movie', 'Select Movie')),
        ),
    ]