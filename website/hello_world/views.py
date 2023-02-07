from django.shortcuts import render


# Create your views here.
def hello_world(request):
    # argument HttpRequestObject is created whenever the page for the url mapped to this view is loaded
    return render(request, 'hello_world.html', {})
    # render looks inside the templates directory inside the app to find the named template to render