from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Welcom to relationship_app page")
