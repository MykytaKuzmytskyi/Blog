from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import NewCommentForm, PostCreateForm, UserCreateForm, PostUpdateForm, UserUpdateForm
from blog.models import Post, Comment


class UserCreationView(generic.CreateView):
    model = get_user_model()
    form_class = UserCreateForm

    def get_success_url(self):
        return reverse("blog:post-list")


class UserUpdateView(generic.UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse("blog:post-list")


class PostListView(generic.ListView):
    model = Post
    form_class = NewCommentForm
    queryset = Post.objects.select_related("author")
    paginate_by = 25

    def get_queryset(self):
        queryset = Post.objects.select_related("author")
        ordering = self.request.GET.get("orderby")
        if ordering == "Username":
            return queryset.order_by(f"author__username")
        if ordering == "Email":
            return queryset.order_by(f"author__email")
        if ordering == "Date":
            return queryset.order_by(f"-publish")
        return queryset


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostUpdateForm

    def get_success_url(self):
        return reverse("post:pots-detail", args=(self.object.id,))


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("post:post-list")


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostCreateForm

    def form_valid(self, form):
        user = self.request.user
        new_post = form.save(commit=False)
        new_post.author_id = user.id
        new_post.save()
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("blog:post-list")


class CommentCreateView(FormMixin, generic.DetailView):
    model = Post
    form_class = NewCommentForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"slug": self.get_object().slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.all()
        context["comment_form"] = NewCommentForm
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, slug):
        user = self.request.user
        post = Post.objects.get(slug=slug['slug'])
        new_comment = form.save(commit=False)
        new_comment.post = post
        new_comment.save()
        return super(CommentCreateView, self).form_valid(form)
