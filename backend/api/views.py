from django.shortcuts import render
from api.models import *
from api.serializer import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [(AllowAny)]
    serializer_class = RegisterSerializer


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def ProtectedView(request):
    if request.method == 'GET':
        response = f'hey {request.user}, GET response'
        return Response({'response':response}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        response = f'hey {request.user},  {text}'
        return Response({'response':response}, status=status.HTTP_200_OK)
    
    return Response({}, status=status.HTTP_400_BAD_REQUEST)

