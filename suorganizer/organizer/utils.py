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
