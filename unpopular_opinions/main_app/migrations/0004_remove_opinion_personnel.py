# Generated by Django 4.2.2 on 2023-06-18 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_opinion_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opinion',
            name='personnel',
        ),
    ]