from distutils.ccompiler import new_compiler
from re import template
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.db.models import Model
from django.core.exceptions import ImproperlyConfigured

class ObjectUpdateMixin:
    form_class = None
    model = None
    template_name = ''


    def get(self, request, slug):
        obj = get_object_or_404(
            self.model, slug__iexact=slug
        )
        context = {
            'form': self.form_class(instance=obj),
            self.model.__name__.lower(): obj
        }
        return render(
            request, self.template_name, context
        )

    def post(self, request, slug):
        obj = get_object_or_404(
            self.model,
            slug__iexact=slug
        )
        bound_form = self.form_class(
            request.POST, instance=obj
        )
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                self.model.__name__.lower(): obj
            }
            return render(
                request,
                self.template_name,
                context
            )

class ObjectDeleteMixin:
    model = None
    success_url = ''
    template_name = ''

    def get(self, request, slug):
        obj = get_object_or_404(
            self.model, slug__iexact=slug
        )
        context = {
            self.model.__name__.lower(): obj
        }
        return render(
            request, self.template_name, context
        )

    def post(self, request, slug):
        obj = get_object_or_404(
            self.model, slug__iexact=slug
        )
        obj.delete()
        return HttpResponseRedirect(self.success_url)

class PageLinksMixin:
    page_kwarg = 'page'

    def first_page(self, page):
        if page.number > 1: 
            return self._page_urls(1)
        return None
    
    def last_page(self, page):
        last_page = page.paginator.num_pages
        if page.number < last_page:
            return self._page_urls(last_page)
        return None

    def _page_urls(self, page_number):
        return "?{pkw}={n}".format(
            pkw=self.page_kwarg,
            n=page_number
        )
    
    def previous_page(self, page):
        if (page.has_previous()
            and page.number > 2):
            return self._page_urls(
                page.previous_page_number()
            )
        return None
    
    def next_page(self, page):
        last_page = page.paginator.num_pages
        if (page.has_next() and page.number < last_page -1):
            return self._page_urls(
                page.next_page_number()
            )
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs
        )
        page = context.get('page_obj')
        if page is not None:
            context.update({
                'previous_page_url': self.previous_page(page),
                'next_page_url': self.next_page(page),
            })
        return context