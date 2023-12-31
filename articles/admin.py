from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]
    list_display = ("title", "date", "author",)
    list_filter = ("date", "author",)
    search_fields = ("title", "body",)
    raw_id_fields = ("author",)
    date_hierarchy = "date"
    ordering = ("date", )
    
    
admin.site.register(Article, ArticleAdmin)

