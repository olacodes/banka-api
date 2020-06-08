from django.http import JsonResponse


def notfound(request):
    message = 'Route provided was not found'
    return JsonResponse(dict(message=message), status=404)
