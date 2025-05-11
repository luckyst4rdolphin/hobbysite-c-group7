from django.views.generic import ListView, DetailView, UpdateView, CreateView
from forum.models import ThreadCategory, Thread, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect

class ThreadListView(LoginRequiredMixin, ListView):
    """
    A view that displays all threads in the system, grouped by category,
    with a separate group for threads authored by the logged-in user.
    """
    template_name = 'thread_list.html'
    context_object_name = 'all_threads'  # used for non-user threads

    def get_queryset(self):
        """
        Return threads not authored by the current user, ordered by category name.
        """
        return Thread.objects.exclude(author=self.request.user.profile).select_related('category').order_by('category__name')

    def get_context_data(self, **kwargs):
        """
        Adds user's threads, all categories, and all other threads to the context.
        """
        context = super().get_context_data(**kwargs)

        # All categories (used for grouping)
        context['categories'] = ThreadCategory.objects.all().order_by('name')

        # Threads created by the logged-in user
        context['user_threads'] = Thread.objects.filter(author=self.request.user.profile).order_by('-created_on')

        return context


class ThreadDetailView(LoginRequiredMixin, DetailView):
    """
    A view that displays the details of a single thread.
    """
    context_object_name = "thread"
    model = Thread
    template_name = 'thread.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch other posts from the same category, excluding the current thread
        category = self.object.category
        related_posts = Thread.objects.filter(category=category).exclude(id=self.object.id)
        context['related_posts'] = related_posts

        # Fetch comments sorted by 'Created On' (oldest first)
        comments = Comment.objects.filter(thread=self.object).order_by('created_on')
        context['comments'] = comments

        return context

class ThreadCreateView(LoginRequiredMixin, CreateView):

