from django.shortcuts import render

from .models import Resource
# Create your views here.

def resource_home(request):
    res = Resource.objects.all()
    context = {
        'res':res,
    }
    return render(request, 'resourcehome.html', context)
