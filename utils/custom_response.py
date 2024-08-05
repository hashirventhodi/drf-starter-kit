from rest_framework.response import Response

class CustomResponse(Response):
    def __init__(self, data=None, status=None, message=None, template_name=None, headers=None, content_type=None, **kwargs):
        is_success = status and status < 400
        response_data = {
            'status': 'success' if is_success else 'error',
            'message': message,
            'data': data if is_success else None,
            'error': data if not is_success else None,
        }
        super().__init__(response_data, status, template_name, headers, content_type)
