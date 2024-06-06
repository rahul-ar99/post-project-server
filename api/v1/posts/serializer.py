from rest_framework import serializers
from posts.models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id","title","created_by", "featured_image")


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['created_by', 'title', 'description','featured_image',]

    def create(self, validate_data):
        post = Post(
            title = validate_data['title'],
            featured_image = validate_data['featured_image'],
            description = validate_data['description'],
            created_by = validate_data['created_by'],
        )
        post.save()
        return post
    
class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        model = ["id","like"]
    
    def add_like(self):
        self.instance.like += 1
        self.instance.save()
        return self.instance.like
    
    def remove_like(self):
        if self.instance.like > 0:
            self.instance.like -= 1
            self.instance.save()
        return self.instance.like
