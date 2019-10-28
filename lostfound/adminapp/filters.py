from mainapp.models import Claim, Post
from bootstrap_datepicker_plus import DateTimePickerInput
import django_filters


class ClaimFilter(django_filters.FilterSet):
    class Meta:
        model = Claim
        fields = ['item_claimed','claimed_by','date_claimed']
        widgets = {
            'date_claimed': DateTimePickerInput(),
        }
    
class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Post
        fields = ['title','When','category']