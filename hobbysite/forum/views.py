from django.views.generic import ListView, DetailView
from forum.models import ThreadCategory, Thread


class ThreadListView(ListView):
    """
    A view that displays all categories, together with their respective threads.
    """

    context_object_name = 'threads'
    queryset = Thread.objects.all()
    template_name = 'thread_list.html'

    
    def get_context_data(self, **kwargs):
        """
        Adds thread categories to the context.
        """
        context = super().get_context_data(**kwargs)
        context['categories'] = ThreadCategory.objects.all()
        return context


class ThreadDetailView(DetailView):
    """
    A view that displays the details of a single thread.
    """
    context_object_name = "thread"
    model = Thread
    template_name = 'thread.html'
