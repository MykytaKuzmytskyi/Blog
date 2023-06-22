from django.urls import path
from .views import PostListView, PostUpdateView, PostDeleteView, PostCreateView, UserCreationView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path("post/update/<slug:slug>/",
         PostUpdateView.as_view(),
         name="post-update"
         ),
    path("post/delete/<slug:slug>/",
         PostDeleteView.as_view(),
         name="post-delete"
         ),
    path("user/create/",
         UserCreationView.as_view(),
         name="user-create"
         ),
]
