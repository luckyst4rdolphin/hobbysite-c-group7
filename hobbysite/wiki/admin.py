from django.contrib import admin
from .models import ArticleCategory, Article

# Register your models here.
class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory

    list_display = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    model = Article

    list_display = ('title', 'category', 'entry', 'created_on', 'updated_on')

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
