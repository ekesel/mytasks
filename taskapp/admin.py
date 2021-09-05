from django.contrib import admin
from .models import *
# Register your models here.

class taskAdmin(admin.ModelAdmin):
    list_display = ('title','desc')
    list_filter = ('user','check')
    search_fields = ('title','user')
    list_per_page = 15

admin.site.register(tasks,taskAdmin)