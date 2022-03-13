from django.shortcuts import render, get_object_or_404

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
    tag = get_object_or_404(Tag, slug__iexact=slug)
    template = loader.get_template('organizer/tag_detail.html')
    context = {'tag': tag}
    return HttpResponse(template.render(context))