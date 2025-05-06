from django.contrib import admin
from forum.models import ThreadCategory, Thread


class ThreadAdmin(admin.ModelAdmin):
    """
    Admin configuration for Thread model.
    """
    model = Thread
    list_display = ('title', 'category', 'created_on',)
    search_fields = ('title',)

class ThreadCategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for ThreadCategory model.
    """
    model = ThreadCategory
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Thread, ThreadAdmin)
admin.site.register(ThreadCategory, ThreadCategoryAdmin)
