from django.shortcuts import render
from .models import Notes

# get notes list
def notes_list(request):
    # render HTML template with notes data
    notes = Notes.objects.all()
    return render(request, "notes/notes_list.html")