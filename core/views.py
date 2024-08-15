from django.shortcuts import render

from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, world. You're at the my_view page.")


# Create your views here.
