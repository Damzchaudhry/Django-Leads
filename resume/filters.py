from .models import Resume
import django_filters
from django.db.models import Q # new

class CvFilter(django_filters.FilterSet):
	exp = django_filters.CharFilter(lookup_expr='icontains')
	skill = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Resume
		fields = [ 'exp','skill',]