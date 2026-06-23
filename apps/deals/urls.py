from django.urls import path
from .views import deals_list

urlpatterns = [
    # if the user goes to /deals/ it will show the deals list
    path("", deals_list),
]