from django.shortcuts import render
from .models import Client

# get clients list
def clients_list(request):
    # render HTML template with clients data
    clients = Client.objects.all()
    return render(request, "clients/clients_list.html", {"clients": clients})