from django.db.models.query import QuerySet
from django.core.paginator import Paginator
from django.core.paginator import Page
from elasticsearch import Elasticsearch
from src.settings import ELASTICSEARCH_AUTH


class CustomPaginator(Paginator):
    OBJECTS_OF_PAGE = 15

    def get_page_range_in_search_template(self, current_page_number: int) -> range:
        if current_page_number > self.num_pages:
            return None

        left_range = max(1, current_page_number - 2)
        right_range = min(current_page_number + 2, self.num_pages) + 1
        return range(left_range, right_range)

    def __init__(self, query_set: QuerySet, *args, **kwargs):
        super(CustomPaginator, self).__init__(
            query_set, self.OBJECTS_OF_PAGE, *args, **kwargs
        )


def get_elasticsearch_client() -> Elasticsearch:
        
    ELASTICSEARCH_HOSTS = [{'host': 'localhost', 'port': 9200}]

    client = Elasticsearch(
        hosts=ELASTICSEARCH_HOSTS,
        http_auth=ELASTICSEARCH_AUTH,
    )
    
    return client