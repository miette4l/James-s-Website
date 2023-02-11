from django.shortcuts import render
from art_collections.models import Collection, Work

# Create your views here.


def collection_index(request):
    art_collections = Collection.objects.all()
    context = {
        'art_collections': art_collections
    }
    # The context dictionary is used to send information to our template.
    # Every view function you create needs to have a context dictionary.
    return render(request, 'collection_index.html', context)
    # Any entries in the context dictionary are available in the template,
    # as long as the context argument is passed to render().
    # You’ll need to create a context dictionary and pass it to render in each view function you create.


def collection_detail(request, pk):
    art_collections = Collection.objects.get(pk=pk)
    context = {
        'art_collections': art_collections
    }
    return render(request, 'collection_detail.html', context)