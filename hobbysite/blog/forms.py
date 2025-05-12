from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    '''
    Creates model form for adding and updating articles.
    '''
    class Meta:
        model = Article
        fields =['title', 'category', 'header_image', 'entry']

class CommentForm(forms.ModelForm):
    '''
    Creates a model form for adding comments.
    '''
    entry = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Say something',}))
    class Meta:
        model = Comment
        fields = ['entry']