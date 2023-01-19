from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *
# Register your models here.

@admin.register(Aktyor)
class AktyorModelAdmin(ModelAdmin):
    search_fields = ['id','ism','davlat']
    list_display = ['id', 'ism', 'davlat', 'jins', 'tugilgan_yil']
    list_display_links = ['id', 'ism']
    list_editable = ['davlat',]
    list_filter = ['jins',]

admin.site.register(Kino)
admin.site.register(Comment)