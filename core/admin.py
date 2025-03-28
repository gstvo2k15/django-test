from django.contrib import admin
from .models import PatchResult

@admin.register(PatchResult)
class PatchResultAdmin(admin.ModelAdmin):
    list_display = ("middleware", "host", "version", "applied", "timestamp")
    list_filter = ("middleware", "applied")
    search_fields = ("host", "version")
    ordering = ("-timestamp",)
