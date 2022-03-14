from django.http import HttpResponse

def index(request):
    return HttpResponse('Heelo ! This is my first django app view')

# Create your views here.
