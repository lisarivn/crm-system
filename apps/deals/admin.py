from django.contrib import admin
from .models import Deal

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "name", "amount", "status")
    list_filter = ("status", "created_at")
    search_fields = ("name", "description")