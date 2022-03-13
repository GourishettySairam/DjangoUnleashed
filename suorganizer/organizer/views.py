from django.shortcuts import render

from django.http.response import HttpResponse, Http404, HttpResponseNotFound
from .models import Tag
from django.template import loader, Context
# Create your views here.

def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = {'tag_list': tag_list}
    output = template.render(context)
    return HttpResponse(output)

def tag_detail(request, slug):
    try:
        tag = Tag.objects.get(slug__iexact=slug)
    except Tag.DoesNotExist:
        raise Http404
        # return HttpResponseNotFound("<h1>Tag not found</h1>")
    template = loader.get_template('organizer/tag_detail.html')
    context = {'tag': tag}
    return HttpResponse(template.render(context))