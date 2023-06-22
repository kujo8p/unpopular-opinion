# Generated by Django 4.2.2 on 2023-06-19 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('rating', models.CharField(choices=[('NC-17', 'Adults only'), ('R', 'Restricted'), ('PG-13', 'Parents Strongly Cautioned'), ('PG', 'Parental Guidance'), ('G', 'General Audiences')], default='NC-17')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tldr', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=10000)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('date', models.DateField(verbose_name='posted on')),
                ('content', models.CharField(max_length=500)),
                ('opinion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.opinion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]