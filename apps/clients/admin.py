from django.contrib import admin
from .models import Client
from apps.notes.models import Notes

# create inline for Notes model to be displayed in Client admin
class NotesInline(admin.TabularInline):
    model = Notes
    extra = 0

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "status")
    inlines = [NotesInline]