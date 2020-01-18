#from django.contrib import admin
from django.contrib import admin
from .models import Post
#registrar modelo para ser visible
admin.site.register(Post)
