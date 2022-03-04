from django.shortcuts import render

from django.http.response import HttpResponse
from .models import Tag
from django.template import loader, Context
# Create your views here.

def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = {'tag_list': tag_list}
    output = template.render(context)
    return HttpResponse(output)