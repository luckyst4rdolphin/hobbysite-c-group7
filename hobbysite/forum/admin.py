from django.contrib import admin
from forum.models import PostCategory, Post


class PostAdmin(admin.ModelAdmin):
    """
    Admin configuration for Post model.
    """
    model = Post
    list_display = ('title',)
    search_fields = ('title',)

class PostCategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for PostCategory model.
    """
    model = PostCategory
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
