from django import forms

from .models import BlogRoom, SongDetails


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogRoom
        fields = ('text',)


class Comment(forms.ModelForm):
    class Meta:
        model = SongDetails
        fields = ('text',)
