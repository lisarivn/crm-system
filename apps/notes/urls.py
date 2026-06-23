from django.urls import path
from .views import notes_list

urlpatterns = [
    # if the user goes to /notes/ it will show the notes list
    path("", notes_list),
]