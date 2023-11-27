from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]
    list_display = ("title", "date", "author",)
    
    
admin.site.register(Article, ArticleAdmin)

