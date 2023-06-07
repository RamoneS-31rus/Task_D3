from django.urls import path
from .views import PostListView, PostDetailView


urlpatterns = [
    path("news/", PostListView.as_view(), name="post_list"),
    path("news/<int:pk>", PostDetailView.as_view(), name="post_detail"),
]
