#!/usr/bin/python

from django.contrib import admin
from django.forms import Textarea, ModelForm
from django.db import models

from .models import *

class EssayAdminForm(ModelForm):
    class Meta:
        model = Essay
        exclude = ['created_at']
        widgets = {
            'abstract':  Textarea(attrs={'rows':10, 'cols':80}),
            'preface':  Textarea(attrs={'rows':10, 'cols':80}),
        }

class EssayAdmin(admin.ModelAdmin):
    form = EssayAdminForm
    list_display = ['title', 'posted_at', 'language', 'category', ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Essay, EssayAdmin)
admin.site.register(Category)
admin.site.register(EssayBundle)
admin.site.register(Language)

