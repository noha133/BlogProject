from rest_framework import serializers
from .models import Post, Like, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "author", "content")
        model = Post


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
