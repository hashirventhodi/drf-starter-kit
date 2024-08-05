from utils.custom_response import CustomResponse
from .serializers import  LoginSerializer, RefreshTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import status

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            response = super().post(request, *args, **kwargs)
            data = {"tokens": response.data}
            return CustomResponse(message="Successfully authenticated", data=data, status=status.HTTP_200_OK)
        else:
            return CustomResponse(message="Please provide valid data", data= serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        serializer = RefreshTokenSerializer(data=request.data)
        if serializer.is_valid():
            response = super().post(request, *args, **kwargs)
            data = {"tokens": response.data}
            return CustomResponse(message="Token refreshed successfully", data=data, status=status.HTTP_200_OK)
        else:
            return CustomResponse(message="Please provide valid data",data= serializer.errors, status= status.HTTP_400_BAD_REQUEST)
