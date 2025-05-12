from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ArticleCategory(models.Model):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class is the model class for Article Category
    This contains the specified parameters for name and description
    required in the specs of the project.

    '''
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        '''
        @authors : Antonth Chrisdale C. Lopez
    
        This class is the Meta inner class of the article category model

        '''
        
        ordering = ['name']
        verbose_name_plural = 'Article Categories'

    def __str__(self):
        '''
        @fn __str__
        @brief returns the title of the object
        '''
        return self.name

class Article(models.Model):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class is the model class for Article
    This contains the specified parameters for title, author,
    category, entry, created_on, and updated_on required in 
    the specs of the project.

    '''

    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="wiki_articles" 
        )
    category = models.ForeignKey(
        ArticleCategory, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )
    entry = models.TextField()
    header_image = models.ImageField(null=False, upload_to="images/")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        '''
        @authors : Antonth Chrisdale C. Lopez
    
        This class is the model class for Article
        This contains the specified parameters for title, author,
        category, entry, created_on, and updated_on required in 
        the specs of the project.

        '''
        ordering = ['-created_on']

    def __str__(self):
        '''
        @fn __str__
        @brief returns the title of the object
        '''
        return self.entry
    
    def get_absolute_url(self):
        '''
        @fn get_absolute_url
        @brief returns url of the article
        '''
        return reverse('wiki:article-detail', args=[self.pk])

class Comment(models.Model):
    '''
    @authors : Antonth Chrisdale C. Lopez
    
    This class is the model class for Comment
    This contains the specified parameters for author, article,
    entry, created_on, and updated_on required in the specs 
    of the project.

    '''
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="wiki_comments" 
        )
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE,
        )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        '''
        @authors : Antonth Chrisdale C. Lopez
   
        This class is the model class for Comment
        This contains the specified parameters for author, article,
        entry, created_on, and updated_on required in the specs 
        of the project.

        '''
        ordering = ['created_on']

