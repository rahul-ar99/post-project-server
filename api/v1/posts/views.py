from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializer import PostSerializers, PostDetailSerializer
from .permission import IsAdminUser
from posts.models import Post




@api_view(["POST"])
@permission_classes([IsAuthenticated])
def posts(request):
    instance = Post.objects.filter(is_deleted=False)

    context = {
        "request":request
    }
    serializer = PostSerializers(instance, many=True, context=context)

    response_data = {
        "status_code":6000,
        "data":serializer.data,
        "message":"this is working",
    }
    return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_post(request, pk):
    instance = Post.objects.get(pk=pk)

    context = {
        "request":request
    }

    serializer = PostDetailSerializer(instance, context=context)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)