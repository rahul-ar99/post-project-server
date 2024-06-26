from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializer import PostSerializers, PostDetailSerializer, PostCreateSerializer, PostLikeSerializer
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
def create_post(request):
    title = request.data['title']
    description = request.data['description']
    image = request.data['image']
    created_by = request.data['created_by']
    data = {
        'title':title,
        'description':description,
        'featured_image':image,
        'created_by':created_by
    }
    context = {
        "request":request
    }
    serializer = PostCreateSerializer(data=data)
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        response_data = {
            "status_code":6000,
            "data":serializer.data,
            "message":"this is working",
        }
        return Response(response_data)
    response_data = {
        "status_code":6001,
        "data":serializer.errors,
        "message":"Invalid Action",
    }
    return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def view(request, pk):
    if Post.objects.filter(pk=pk).exists():
        instance = Post.objects.get(pk=pk)
        context = {
            'request':request
        }
        serializer = PostDetailSerializer(instance, context=context)
        response_data = {
            "status_code":6000,
            "data":serializer.data,
            "message":"this is working",
        }
        return Response(response_data)
    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like(request, pk):
    if Post.objects.filter(pk=pk).exists():
        instance = Post.objects.get(pk=pk)
        action = request.data['action']
        serializer = PostLikeSerializer(instance)
        if action == "like":
            new_like_count = serializer.add_like()
        elif action == "unlike":
            new_like_count = serializer.remove_like()
        else:
            response_data = {
                "status_code":6001,
                "message":"Invalid action",
            }
            return Response(response_data)
        response_data = {
            "status_code":6000,
            "data":{"like":new_like_count},
            "message":"Invalid action",
        }
        return Response({"newLikeCount":new_like_count}, status=status.HTTP_200_OK)
    else:
        response_data = {
            "status_code":6001,
            "message":"Your given id is not valid",
        }
        return Response(response_data)
