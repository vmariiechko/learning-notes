from django.contrib import admin
from .models import Article, Comment


# class CommentIncline(admin.StackedInline):
class CommentIncline(admin.TabularInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentIncline
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
