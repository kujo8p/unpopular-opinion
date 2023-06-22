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

    if 'person' in self.data:
      try:
          person_id = int(self.data.get('person'))
          self.fields['movie'].queryset = Personnel.objects.get(id=person_id).movies.all().order_by('title')
      except (ValueError, TypeError):
        pass
    elif self.instance.pk:
      self.fields['movie'].queryset = self.instance.person.movie_set.order_by('title')

  class Meta:
    model = Opinion
    fields = ['person', 'movie', 'person_role', 'tldr', 'content']