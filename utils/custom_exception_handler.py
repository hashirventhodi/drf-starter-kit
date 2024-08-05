from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

from .custom_response import CustomResponse

def custom_exception_handler(exc, context):
    # Delegate exception handling to default DRF exception handler
    response = exception_handler(exc, context)
    print (f"Exception {exc}")

    if response is not None:
        # Check if the exception is related to JWT authentication
        if 'detail' in response.data:
            return CustomResponse(message=response.data['detail'], status=response.status_code)
    
    # If response is None, build a custom error response
    error_message = "An error occurred."  # Default error message
    if hasattr(exc, 'detail'):
        error_message = exc.detail  # Extract error detail if available

    # You may want to customize the error message further based on the exception type

    return CustomResponse(message=error_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
