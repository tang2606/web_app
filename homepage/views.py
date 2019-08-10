from django.shortcuts import render, get_object_or_404
from .models import Homepage
# Create your views here.


def home_text(request,tempid):
    hemo_page = get_object_or_404(Homepage, pk=tempid)

    return render(request, 'home_text.html', {'hp': hemo_page})