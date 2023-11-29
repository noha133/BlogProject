from django.urls import path
from .views import PostList, PostCreate,PostDetail, CommentCreateAPIView, LikeToggleAPIView


urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="detailcreate"),
    path("list/", PostList.as_view(), name="listcreate"),
    path("create/", PostCreate.as_view(), name="listcreate"),
    path("<int:pk>/comments/", CommentCreateAPIView.as_view(), name="comment-create"),
    path("<int:pk>/toggle-like/", LikeToggleAPIView.as_view(), name="like-toggle"),
]
