from django.forms import ModelForm, ModelChoiceField
from .models import Comment, Opinion, Movie, Personnel

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
    fields = ['movie_choice', 'tldr', 'content']

class OpinionFormPerson(ModelForm):
  def __init__(self, *args, **kwargs):
    super(OpinionForm, self).__init__(*args, **kwargs)
    self.fields['person_choice'] = ModelChoiceField(queryset=Personnel.objects.all()) 
    self.fields['person_movie'] = ModelChoiceField(queryset=Personnel.movie_set.all())

  class Meta:
    model = Opinion
    fields = ['person_choice', 'person_movie', 'person_role', 'tldr', 'content']