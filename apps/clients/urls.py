from django.urls import path
from .views import clients_list

urlpatterns = [
    # if the user goes to /clients/ it will show the clients list
    path("", clients_list),
]