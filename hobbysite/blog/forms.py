from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =['title', 'category', 'header_image', 'entry']

class CommentForm(forms.ModelForm):
    entry = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Say something',}))
    class Meta:
        model = Comment
        fields = ['entry']