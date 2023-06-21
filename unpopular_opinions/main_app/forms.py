from django.forms import ModelForm, ModelChoiceField
from .models import Comment, Opinion, Movie, Personnel

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']


class OpinionForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(OpinionForm, self).__init__(*args, **kwargs)


  class Meta:
    model = Opinion
    fields = ['movie', 'tldr', 'content']


class OpinionFormPerson(ModelForm):
  def __init__(self, *args, **kwargs):
    super(OpinionFormPerson, self).__init__(*args, **kwargs)
    self.fields['movie'].queryset = Movie.objects.none()

  class Meta:
    model = Opinion
    fields = ['person', 'movie', 'person_role', 'tldr', 'content']