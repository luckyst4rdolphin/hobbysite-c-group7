from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Thread categories'

    def __str__(self):
        return self.name


class Thread(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ThreadCategory,
        on_delete = models.SET_NULL,
        null = True
    )
    author = models.ForeignKey(
        Profile,
        on_delete = models.SET_NULL,
        null = True,
        related_name = "forum_threads"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forum:thread-detail', args=[self.pk])


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete = models.SET_NULL,
        null = True,
        related_name = "forum_comments"
    )
    thread = models.ForeignKey(
        Thread,
        on_delete = models.CASCADE
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
