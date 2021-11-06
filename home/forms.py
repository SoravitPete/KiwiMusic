from django import forms

from .models import BlogRoom


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogRoom
        fields = ('text', )
