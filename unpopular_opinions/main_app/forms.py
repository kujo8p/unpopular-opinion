from django.forms import ModelForm, ModelChoiceField
from .models import Comment, Opinion, Movie

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']


class OpinionForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(OpinionForm, self).__init__(*args, **kwargs)
    self.fields['movie_choice'] = ModelChoiceField(queryset=Movie.objects.all())

  class Meta:
    model = Opinion
    fields = ['tldr', 'content', 'movie_choice']