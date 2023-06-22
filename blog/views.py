from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import NewCommentForm, PostCreateForm, UserCreateForm, PostUpdateForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    form_class = NewCommentForm
    queryset = Post.objects.select_related("author")
    paginate_by = 25


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostUpdateForm

    def get_success_url(self):
        return reverse("post:pots-detail", args=(self.object.id,))


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("post:post-list")

