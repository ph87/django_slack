from django.contrib import admin

# Register your models here.
from .models import Command

class CommandAdminModel(admin.ModelAdmin):
    list_display = ['id', 'command', 'description', 'is_enabled']
    list_filter = ['is_enabled']
    search_fields= ['command', 'code']


admin.site.register(Command, CommandAdminModel)
