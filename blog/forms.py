from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Comment, Post, User
from mptt.forms import TreeNodeChoiceField


class UserCreateForm(UserCreationForm):
    avatar = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "email",
            "first_name",
            "last_name",
            "avatar",
        )


class PostCreateForm(forms.ModelForm):
    email = forms.EmailField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = Post
        fields = ("title", 'email', 'content', 'captcha')


class PostUpdateForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "captcha",
        ]


class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ('name', 'parent', 'email', 'content')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'email': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(NewCommentForm, self).save(*args, **kwargs)
