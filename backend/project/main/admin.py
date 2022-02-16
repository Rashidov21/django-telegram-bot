from django.contrib import admin
from .models import Words
# Register your models here.

class WordsAdmin(admin.ModelAdmin):
    """Word Admin Class"""
    list_display = ['pk','word','gender']
    list_editable = ['word','gender']


admin.site.register(Words, WordsAdmin)