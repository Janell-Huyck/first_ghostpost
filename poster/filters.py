import django_filters
from .models import GhostPost


class PostFilter(django_filters.FilterSet):

    class Meta:
        model = GhostPost
        fields = ('title', 'text')
