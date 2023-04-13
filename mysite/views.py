from django.http import HttpResponse,JsonResponse
def hello(request):
    
    return HttpResponse(5)
def jason(request):
    return JsonResponse({'alireza': 24})