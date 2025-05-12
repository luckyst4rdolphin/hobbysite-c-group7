from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ArticleCategory(models.Model):
    '''
    Accepts name of category and description of category.
    '''
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Article categories"

    def __str__(self):
        return self.name
    
class Article(models.Model):
    '''
    Accepts title of article, category of article in connection to ArticleCategory model, 
    author of article in connection to Profile model, header image for the article, and article content
    '''
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        blank = True,
        null = True,
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="blog_articles"
    )
    header_image = models.ImageField(null=True, upload_to="images/")
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.entry
    
    def get_absolute_url(self):
        return reverse('blog:article-detail', args=[self.pk])
    
class Comment(models.Model):
    '''
    Accepts author of comment in connection to Profile model,
    article commented on in connection to Article model,
    and comment content.
    '''
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
