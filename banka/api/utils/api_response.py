from django.http import JsonResponse


class APIResponse:
    def __init__(self):
        self.status_code = None
        self.message = None
        self.error = None
        self.data = None
        self.type = None

    def set_success(self, status_code, message, data):
        self.status_code = status_code
        self.message = message
        self.data = data
        self.type = 'success'

    def set_error(self, status_code, message, error):
        self.status_code = status_code
        self.message = message
        self.error = error
        self.type = 'error'

    def send(self):
        if self.type == 'error':
            error_result = {
                'status': self.status_code,
                'message': self.message,
                'error': self.error,
            }
            return JsonResponse((error_result), status=self.status_code)
        elif self.type == 'success':
            success_result = {
                'status': self.status_code,
                'message': self.message,
                'data': {
                    self.data
                }
            }
            return JsonResponse((success_result), status=self.status_code)

        return JsonResponse(dict(message='Internal Server Error'), status=500)
