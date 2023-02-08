from django.shortcuts import render
from art_collections.models import Collection, Work

# Create your views here.


def collection_index(request):
    art_collections = Collection.objects.all()
    context = {
        'art_collections': art_collections
    }
    return render(request, 'collection_index.html', context)


def collection_detail(request, pk):
    art_collections = Collection.objects.get(pk=pk)
    context = {
        'art_collections': art_collections
    }
    return render(request, 'collection_detail.html', context)