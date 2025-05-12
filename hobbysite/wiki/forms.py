from django import forms
from .models import Article, Comment
 
class ArticleCreateForm(forms.ModelForm):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class contains the form for creating Articles

    '''
    class Meta:
        '''
        @authors : Antonth Chrisdale C. Lopez
    
        This class contains the form for creating Articles

        '''
        model = Article
        fields = "__all__"

class ArticleUpdateForm(forms.ModelForm):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class contains the form for updating existing
    Articles.

    '''
    class Meta:
        '''
        @authors : Antonth Chrisdale C. Lopez
    
        This class contains the form for updating existing
        Articles.

        '''
        model = Article
        fields = ['title', 'category', 'entry', 'header_image', 'updated_on']

class CommentForm(forms.ModelForm):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class contains the form for creating Comments

    '''
    entry = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Add a comment',}))
    class Meta:
        model = Comment
        fields = ['entry']