from .models import Post
import django_filters

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Post
        fields = ['title','When','category']

