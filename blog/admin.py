from django.contrib import admin
from . import models


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email',  'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')