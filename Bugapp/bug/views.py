from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at Tuck Wai's bug app index.")