from django.contrib import admin
from .models import Post #z biblioteki models importuj, klasę Post
#uwaga! nazwa klasy pisana z wielkiej litery!

# Register your models here.
admin.site.register(Post)
