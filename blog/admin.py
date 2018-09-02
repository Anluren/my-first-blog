from django.contrib import admin
# relative import from models.py
from .models import Post

# Register your models here.
admin.site.register(Post)
