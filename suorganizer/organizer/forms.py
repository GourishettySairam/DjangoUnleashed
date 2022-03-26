from django import forms
from .models import Tag
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        # fields = "__all__"
        exclude = ['slug']
        fields = ['name', 'slug']
    
    def clean_name(self):
        return self.cleaned_data['name'].lower()

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == "create":
            raise ValidationError('Slug may not be "create"')
        return new_slug