from django.shortcuts import render

from apps.clients.models import Client
from apps.deals.models import Deal
from apps.notes.models import Notes


def dashboard(request):
    context = {
        "clients_count": Client.objects.count(),
        "deals_count": Deal.objects.count(),
        "notes_count": Notes.objects.count(),
    }

    return render(request, "dashboard/dashboard.html", context)