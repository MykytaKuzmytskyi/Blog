from django.urls import path
from .views import PostListView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path("post/update/<slug:slug>/",
         PostUpdateView.as_view(),
         name="post-update"
         ),
    path("post/delete/<slug:slug>/",
         PostDeleteView.as_view(),
         name="post-delete"
         ),
]
