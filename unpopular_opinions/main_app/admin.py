from django.contrib import admin
from .models import Movie, Personnel, Opinion, Comment

# Register your models here.
admin.site.register(Movie)
admin.site.register(Personnel)
admin.site.register(Opinion)
admin.site.register(Comment)