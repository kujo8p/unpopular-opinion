# Generated by Django 4.2.2 on 2023-06-21 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_opinion_movie_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='movie_choice',
            field=models.CharField(choices=[('Select Movie', 'Select Movie'), (2, 'It'), (1, 'Interstellar'), (9, 'Minority Report'), (10, 'Arrival'), (12, 'Tron'), (13, 'Tron: Legacy'), (14, 'Tenet')], default=('Select Movie', 'Select Movie')),
        ),
    ]
