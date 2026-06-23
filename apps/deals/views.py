from django.shortcuts import render
from .models import Deal

# get deals list
def deals_list(request):
    # render HTML template with deals data
    deals = Deal.objects.all()
    return render(request, "deals/deals_list.html", {"deals": deals})