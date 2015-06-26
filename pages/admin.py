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
            'preface':  Textarea(attrs={'rows':10, 'cols':80}),
        }

class EssayAdmin(admin.ModelAdmin):
    form = EssayAdminForm
    list_display = ['title', 'posted_at', 'all_tags', 'language', ]
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags', )


admin.site.register(Essay, EssayAdmin)
admin.site.register(Tag)
admin.site.register(EssayBundle)
admin.site.register(Language)
