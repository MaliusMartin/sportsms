from django.contrib import admin

# Register your models here.
from .models import Sport, Category, Post,Detail, Author

admin.site.register(Sport)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Detail)
admin.site.register(Author)