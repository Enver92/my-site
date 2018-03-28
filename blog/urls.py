from django.urls import path

from .views import PostListView, PostDetailView

app_name = "blog"

urlpatterns = [
    path("posts", PostListView.as_view(), name='posts'),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
]
