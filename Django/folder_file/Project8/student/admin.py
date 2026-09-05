from django.contrib import admin
from .models import Student
# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdminList(admin.ModelAdmin):
      list_display = ['id','name','city']
      search_fields = ['city']
      list_filter = ['id']
      ordering = ('id',)