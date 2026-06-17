from django.contrib import admin
from .models import Notes


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "deal", "note_type", "created_at")