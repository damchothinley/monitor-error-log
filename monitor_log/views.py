from django.http import HttpResponse  # newly added

# Create your views here.


def HomePageView(request):
    return HttpResponse("Hello World!")


def ErrorView(request):
    error = ""
    if error:
        return HttpResponse(error)
