from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created', 'status']
    list_filter = ['created', 'status']
    search_fields = ['author', 'title', 'description']
    raw_id_fields = ['author']
    prepopulated_fields = {'slug': ['title']}
