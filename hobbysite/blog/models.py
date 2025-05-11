from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ArticleCategory(models.Model):
    '''
    Contains data for possible article categories.
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
    Contains data for each article.
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
    )
    header_image = models.ImageField(null=False, upload_to="images/")
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
        ordering = ["created_on"]
