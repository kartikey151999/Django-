from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','completed','createdAt')
    list_filter = ('completed','createdAt')
    search_fields = ('title','description')
    ordering = ('-createdAt',)