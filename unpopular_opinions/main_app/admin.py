from django.contrib import admin
<<<<<<< HEAD
from .models import Movie, Personnel, Opinion, Comment

# Register your models here.
admin.site.register(Movie)
admin.site.register(Personnel)
admin.site.register(Opinion)
admin.site.register(Comment)
=======
from .models import Movie, Personnel, Comment, Opinion

# Register your models here.
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Opinion)
admin.site.register(Personnel)
>>>>>>> 095e4436ac7515d6b4ba49a4bc0454c3abf4508c
