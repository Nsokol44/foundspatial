from django.shortcuts import render, get_object_or_404

from .models import Publication


def publication_home(request):
    pubs = Publication.objects.order_by('-datetime')
    context = {
        'pubs':pubs,
    }
    return render(request, 'publicationhome.html', context)
