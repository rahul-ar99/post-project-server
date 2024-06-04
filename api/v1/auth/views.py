from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from authuser.models import User
from . serializers import UserSerializers , UserCreateSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def show(request):
    instance = User.objects.all()
    serializer = UserSerializers(instance, many=True)
    response_data={
        "status_code":6000,
        "data":serializer.data
    }
    return Response(response_data)


@api_view(['POST'])
@permission_classes([AllowAny])
def create(request):
    username = request.data['username']
    email = request.data['email']
    role = request.data['role']
    password = request.data['password']

    instance = User.objects.all()
    serializer = UserSerializers(instance, many=True)
    if(User.objects.filter(username=username)).exists():
        response_data={
            "status_code":6000,
            "data":serializer.data,
            "message":"user already exist"
        }
        return Response(response_data)
    data = {
        'username': username,
        'email': email,
        'role': role,
        'password': password
    }
    serializer = UserCreateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        response_data={
            "status_code":2000,
            "data":serializer.data
        }
        return Response(response_data, status=201)
    else:
        response_data={
            "status_code":2001,
            "data":serializer.errors
        }
        return Response(response_data, status=400)