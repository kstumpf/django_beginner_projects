# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# This function has been replaced by the class PostListView.
def blog_list(request, *args, **kwargs):
    post_list = Post.objects.filter(published=True)
    template_name = "post_list.html"
    context = {
        "post_list": post_list
    }

    return render(request, template_name, context)

# This function has been replaced by the class PostDetailView.
def blog_detail(request, pk, *args, **kwargs):
    post = Post.objects.get(pk=pk, published = True)
    template_name = "blog/post_detail.html"

    context = {
        "post": post
    }

    return render(request, template_name, context)


class PublishedPostsMixin(object):
    def get_queryset(self):
        return self.model.objects.live()


class PostListView(PublishedPostsMixin, ListView):
    model = Post


class PostDetailView(PublishedPostsMixin, DetailView):
    model = Post
