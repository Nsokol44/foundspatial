from django.shortcuts import render
from .models import Bio

# Create your views here.

def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    bios = Bio.objects.order_by('datetime')
    context = {
        'bios':bios,
    }
    return render(request, 'about.html', context = context)
