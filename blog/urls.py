from django.urls import path
from .views import PostList, PostDetail, CommentCreateAPIView, LikeToggleAPIView


urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="detailcreate"),
    path("", PostList.as_view(), name="listcreate"),
    path("<int:pk>/comments/", CommentCreateAPIView.as_view(), name="comment-create"),
    path("<int:pk>/toggle-like/", LikeToggleAPIView.as_view(), name="like-toggle"),
]
