from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms


from .models import Post


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
