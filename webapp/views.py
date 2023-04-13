from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def home(request):
    return HttpResponse("Home")

def about(request):
    return HttpResponse("I am Alireza Ansari , I am a programmer ;)")
def contact(request):
    return JsonResponse({"alireza":"ansari"},{"number":"09172215452"})