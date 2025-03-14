from django.contrib import admin
from .models import Commission, Comment

# Register your models here.
class CommissionAdmin(admin.ModelAdmin):
    '''
    Admin configurationn for the commission model.
    '''
    model = Commission
    list_display = ('title', 'people_required', 'created_on', 'updated_on')

class CommentAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the comment model.
    '''
    model = Comment
    list_display = ('commission', 'entry', 'created_on', 'updated_on')

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)