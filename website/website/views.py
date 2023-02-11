from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    html = "<html><body>James nice website</body></html>"
    return HttpResponse(html)
    # I want home to have links to the 3 apps: art_collections, blog_1, blog_2