from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Haroon loves you if you are seeing this ")