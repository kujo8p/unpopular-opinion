from rest_framework import serializers
from base.models import discover_movies


class MovieSerializer(serializers.ModelSerializer):
    class meta:
        model = Movie
        fields = "__all__"
