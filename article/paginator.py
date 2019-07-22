from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )




class ArticleApiPagination(LimitOffsetPagination):
	default_limit = 2
	max_limit=5
		