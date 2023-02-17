from django.contrib import admin
from .models import *
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')



admin.site.register(Post, AuthorAdmin)