from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email')
    list_display_links = ('id', 'firstname', 'lastname', 'email')
    list_filter = ('id', 'firstname', 'lastname', 'email')
    search_fields = ('id', 'firstname', 'lastname', 'email')
    list_per_page = 15

admin.site.register(Teacher, TeacherAdmin)
