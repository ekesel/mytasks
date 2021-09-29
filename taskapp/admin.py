from django.contrib import admin
from .models import *
# Register your models here.

class taskAdmin(admin.ModelAdmin):
    list_display = ('title','desc')
    list_filter = ('user','check')
    search_fields = ('title','user')
    list_per_page = 15


class streakAdmin(admin.ModelAdmin):
    list_display = ('count','user')
    list_filter = ('user',)
    search_fields = ('user',)
    list_per_page = 15

admin.site.register(tasks,taskAdmin)

admin.site.register(streak,streakAdmin)