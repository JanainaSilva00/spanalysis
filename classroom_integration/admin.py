from django.contrib import admin
from .models import Credentials


class CredentialAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'api_key')
    list_display_links = ('client_id', 'api_key')
    list_filter = ('client_id', 'api_key')
    search_fields = ('client_id', 'api_key')
    list_per_page = 15

admin.site.register(Credentials, CredentialAdmin)
