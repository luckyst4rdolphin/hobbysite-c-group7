from django.contrib import admin
from .models import ArticleCategory, Article, Comment

class ArticleCategoryAdmin(admin.ModelAdmin):
    '''
    @authors : Antonth Chrisdale C. Lopez

    This class is the admin class of the ArticleCategory model.

    '''
    model = ArticleCategory

    list_display = ('name',)

class CommentInline(admin.StackedInline):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class is the admin class of the Comment model which is kept
    inside the Article

    '''
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class is the admin class of the Article model.

    '''
    model = Article

    list_display = ('title', 'category', 'entry', 'created_on', 'updated_on')
    inlines = [CommentInline,]

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
