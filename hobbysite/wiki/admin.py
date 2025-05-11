from django.contrib import admin
from .models import ArticleCategory, Article, Comment

class ArticleCategoryAdmin(admin.ModelAdmin):
    '''
    @authors : Antonth Chrisdale C. Lopez

    This class is the admin class of the ArticleCategory model.

    '''
    model = ArticleCategory

    list_display = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class is the admin class of the Article model.

    '''
    model = Article

    list_display = ('title', 'author', 'category', 'entry', 'header_image', 'created_on', 'updated_on')

class CommentAdmin(admin.ModelAdmin):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class is the admin class of the Comment model.

    '''
    model = Comment

    list_display = ('author', 'article', 'entry', 'created_on', 'updated_on')

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
