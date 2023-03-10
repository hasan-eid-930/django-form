from django.contrib import admin
from .models import Blog,Article,Person,Author,Image

# Register your models here.

admin.site.register(Author)
admin.site.register([Article,Blog,Person,Image])