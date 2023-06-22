from django.contrib import admin
from .models import Movie, Personnel

# Register your models here.
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Opinion)
admin.site.register(Personnel)
