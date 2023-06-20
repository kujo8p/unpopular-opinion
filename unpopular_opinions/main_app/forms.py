from django.forms import ModelForm
from .models import Comment, Opinion

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']


class OpinionForm(ModelForm):
  class Meta:
    model = Opinion
    fields = ['tldr', 'content']