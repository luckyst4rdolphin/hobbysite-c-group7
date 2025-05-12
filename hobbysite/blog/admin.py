from django.contrib import admin
from .models import ArticleCategory, Article, Comment

class ArticleCategoryAdmin(admin.ModelAdmin):
    '''
    This is the admin panel for the Article Category model.
    '''
    model = ArticleCategory

    list_display = ('name', )

class CommentInline(admin.StackedInline):
    model = Comment
    
class ArticleAdmin(admin.ModelAdmin):
    '''
    This is the admin panel for the Article model.
    '''
    model = Article

    list_display = ('title', 'category', 'entry', 'created_on', 'updated_on')
    inlines = [CommentInline,]



admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
