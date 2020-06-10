from django.http import JsonResponse


def notfound(request):
    message = 'Route provided was not found'
    return JsonResponse(dict(message=message), status=404)

def index(request):
    message = 'Welcome to Banka Rest API'
    return JsonResponse(dict(message=message), status=200)

def home(request):
    message = 'You are not expected to be here, visit /api/v1/'
    return JsonResponse(dict(message=message), status=403)
