from django import forms

from .models import PostProfile, PostComment


class PostForm(forms.ModelForm):
    post = forms.CharField(
        required=True,
        label="",
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Post something...',
                'class': 'form-control small-title'
                }),)
    title = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Title...',
                'class': 'form-control small'
            }),)

    class Meta:
        model = PostProfile
        exclude = ('user', 'user_like', 'user_dislike', 'comment',)


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Comment...',
                'class': 'form-control small'
                }),)

    class Meta:
        model = PostComment
        exclude = ('user_comment',)
