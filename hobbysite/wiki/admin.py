from django.contrib import admin
from .models import ArticleCategory, Article

# Register your models here.
class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory

class ArticleAdmin(admin.ModelAdmin):
    model = Article

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
