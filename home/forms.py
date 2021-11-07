from django import forms

from .models import BlogRoom, BlogRoomComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogRoom
        fields = ('text', )


class Comment(forms.ModelForm):
    class Meta:
        model = BlogRoomComment
        fields = ('comment', )
