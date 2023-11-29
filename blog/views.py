from rest_framework import generics
from .permissions import PostUserWritePermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from user.permissions import AdminPermission, AuthorPermission, ReaderPermission


class PostList(generics.ListAPIView):
    permission_classes = [ReaderPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["content", "title"]
    filterset_fields = {
        "author__first_name": ["exact"],
        "category__name": ["exact"],
        "published": ["date__lte", "date__gte", "date__exact"],
    }


class PostCreate(generics.CreateAPIView):
    permission_classes = [AuthorPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [AuthorPermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class CommentCreateAPIView(generics.CreateAPIView):
    permission_classes = [ReaderPermission]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_pk = self.kwargs.get("pk")
        post = Post.objects.get(pk=post_pk)
        serializer.save(user=self.request.user, post=post)


class LikeToggleAPIView(APIView):
    permission_classes = [ReaderPermission]
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        # Check if the user has already liked the post
        like_exists = Like.objects.filter(user=user, post=post).exists()

        if like_exists:
            # If liked, unlike
            Like.objects.filter(user=user, post=post).delete()
        else:
            # If not liked, like
            Like.objects.create(user=user, post=post)

        return Response({"detail": "Operation successful"}, status=status.HTTP_200_OK)
