from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify

from .models import DroneFootage

# Create your views here.

def drone_view(request):
    droneposts = DroneFootage.objects.order_by('-datetime')
    context = {
        'droneposts':droneposts,
    }
    return render(request, 'dronehome.html', context)

def drone_detail(request, slug):
    dronepost = get_object_or_404(DroneFootage, slug=slug)
    context = {
        'dronepost':dronepost,
    }
    return render(request, 'dronedetail.html', context)
