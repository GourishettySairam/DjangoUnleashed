from django.shortcuts import (get_object_or_404, redirect, render)

from django.http.response import HttpResponse, Http404, HttpResponseNotFound
from django.urls import reverse, reverse_lazy

from .forms import NewsLinkForm, TagForm, StartupForm
from .models import Startup, Tag, NewsLink
from django.template import loader, Context
from django.views.generic import View

# from .utils import ObjectDeleteMixin, ObjectUpdateMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, CreateView, DeleteView

from core.utils import UpdateView

# Create your views here.

def tag_list(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})

class TagList(View):
    template_name = 'organizer/tag_list.html'

    def get(self, request):
        tags = Tag.objects.all()
        context = {
            'tag_list': tags,
        }
        return render(
            request, self.template_name, context
        )
    
class TagPageList(View):
        paginate_by = 5
        template_name = 'organizer/tag_list.html'

        def get(self, request, page_number):
            tags = Tag.objects.all()
            paginator = Paginator(
                tags, self.paginate_by
            )

            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(
                    paginator.num_pages
                )
            
            if page.has_previous():
                prev_url = reverse(
                    'organizer_tag_page',
                    args={
                        page.previous_page_number()
                    }
                )
            else:
                prev_url = None
            if page.has_next():
                next_url = reverse(
                    'organizer_tag_page',
                    args={
                        page.next_page_number()
                    }
                )
            else:
                next_url = None
            
            context = {
                'is_paginated': page.has_other_pages(),
                'next_page_url': next_url,
                'paginator': paginator,
                'previous_page_url': prev_url,
                'tag_list': page
            }

            return render(
                request,
                self.template_name,
                context
            )


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'organizer/tag_detail.html', {'tag': tag})

class StartupDetail(DetailView):
    model = Startup

class TagDetail(DetailView):
    model = Tag

class StartupList(View):
    page_kwarg = 'page'
    paginate_by = 5
    template_name = 'organizer/startup_list.html'

    def get(self, request):
        startups = Startup.objects.all()
        paginator = Paginator(startups, self.paginate_by)
        page = None
        page_number = request.GET.get(
            self.page_kwarg
        )
        prev_url = None
        next_url = None
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            print(paginator.page(1))
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages
            )
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n = page.previous_page_number()
            )
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number()
            )
        else:
            next_url = None
        
        context = {
            'is_paginated': page.has_other_pages(),
            'paginator': paginator,
            'startup_list': page,
            'next_page_url': next_url,
            'previous_page_url': prev_url
        }
        return render(
            request,
            self.template_name,
            context
        )

def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request, 'organizer/startup_detail.html', {'startup': startup})

def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
        else:
            form = TagForm()
        return render(
            request,
            'organizer/tag_form.html',
            {'form': form}
        )

class TagCreate(CreateView):
    form_class = TagForm
    model = Tag


class StartupCreate(CreateView):
    form_class = StartupForm
    model = Startup


class NewsLinkCreate(CreateView):
    form_class = NewsLinkForm
    model = NewsLink

class NewsLinkUpdate(UpdateView):
    form_class = NewsLinkForm
    model = NewsLink
    template_name_suffix = '_form_update'


class TagUpdate(UpdateView):
    form_class = TagForm
    model = Tag
    template_name_suffix = "_form_update"

class TagDelete(DeleteView, View):
    model = Tag
    success_url = reverse_lazy(
        'organizer_tag_list'
    )

class StartupUpdate(UpdateView):
    form_class = StartupForm
    model = Startup
    template_name_suffix = "_form_update"

class StartupDelete(DeleteView, View):
    model = Startup
    success_url = reverse_lazy(
        'organizer_startup_list'
    )

class NewsLinkDelete(DeleteView):
    
    def get(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk
        )
        return render(
            request,
            'organizer/'
            'newslink_confirm_delete.html',
            {'newslink': newslink}
        )
    
    def post(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk
        )
        startup = newslink.startup
        newslink.delete()
        return redirect(startup)
    
    def get_success_url(self):
        return (
            self.object.startup.get_absolute_url()
        )

def model_list(request, model):
    context_object_name = '{}_list'.format(
        model._meta.model_name
    )
    context = {
        context_object_name: model.objects.all()
    }
    template_name = (
        'organizer/{}_list.html'.format(
            model._meta.model_name
        )
    )
    return render(request, template_name, context)