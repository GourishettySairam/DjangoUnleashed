from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, CreateView, YearArchiveView, MonthArchiveView, ArchiveIndexView, DetailView, DeleteView
from jupyterlab_server import slugify
from .models import Post

from django.views.decorators.http import require_http_methods
from .forms import PostForm
from .utils import PostGetMixin
from core.utils import UpdateView
from django.urls import reverse, reverse_lazy

# Create your views here

class PostUpdate(PostGetMixin, UpdateView):
    form_class = PostForm
    model = Post


class PostDelete(PostGetMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog_post_list')

class PostCreate(CreateView):
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form})


class PostList(ArchiveIndexView):
    template_name = 'blog/post_list.html'
    allow_empty = True
    allow_future = True
    context_object_name = "post_list"
    date_field = "pub_date"
    make_object_list = True
    model = Post
    paginate_by = 5

    def get(self, request):
        return render(request, self.template_name, {'post_list': Post.objects.all()})


class PostDetail(PostGetMixin, DetailView):
    model = Post


class PostArchiveYear(YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list: True

class PostArchiveMonth(MonthArchiveView):
    model = Post
    date = 'pub_date'
    month_format = '%m'
