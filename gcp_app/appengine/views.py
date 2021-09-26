from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is Callista's test app to deploy using app engine")