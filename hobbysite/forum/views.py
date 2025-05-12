from django.views.generic import ListView, DetailView, UpdateView, CreateView
from forum.models import ThreadCategory, Thread, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from .forms import ThreadForm, CommentForm

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

        # Add a link to go back to the thread list view
        context['back_to_list_url'] = reverse('forum:thread-list')

        # Add edit link if the user is the author of the thread
        if self.object.author == self.request.user.profile:
            context['edit_url'] = reverse('forum:thread-edit', args=[self.object.pk])

        return context

    def post(self, request, *args, **kwargs):
        """
        Handle comment form submission.
        """
        thread = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            # Associate the comment with the thread and the logged-in user
            form.instance.thread = thread
            form.instance.author = request.user.profile
            form.save()

            # Redirect back to the thread detail page
            return redirect('forum:thread-detail', pk=thread.pk)

        # If the form is invalid, re-render the thread detail view with the form errors
        context = self.get_context_data(**kwargs)
        context['comment_form'] = form
        return self.render_to_response(context)


class ThreadCreateView(LoginRequiredMixin, CreateView):

    model = Thread
    template_name = "thread_form.html"
    form_class = ThreadForm
    success_url = reverse_lazy('forum:thread-list')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ThreadCreateView, self).get_context_data(**kwargs)
        context['thread_form'] = context['form']
        return context


class ThreadUpdateView(LoginRequiredMixin, UpdateView):

    model = Thread
    template_name = "thread_form.html"
    form_class = ThreadForm
    success_url = reverse_lazy('forum:thread-list')

    def get_queryset(self):
        # Only allows the respective thread author to edit the thread
        return Thread.objects.filter(author=self.request.user.profile)
