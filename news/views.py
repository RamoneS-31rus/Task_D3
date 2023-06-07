from django.views.generic import ListView, DetailView

from .models import Post, Category


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'    
    ordering = '-date_create'
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
