from django.db.models.query import QuerySet
from django.core.paginator import Paginator


class CustomPaginator(Paginator):
    
    OBJECTS_OF_PAGE = 15

    def get_page_range(self, current_page_number: int) -> range:        
        left_range = max(1, current_page_number - 2)
        right_range = min(current_page_number + 2, self.num_pages) + 1

        return range(left_range, right_range)

    def __init__(self, query_set: QuerySet, *args, **kwargs):
        super(CustomPaginator, self).__init__(
            query_set, self.OBJECTS_OF_PAGE, *args, **kwargs
        )
        
    
    @staticmethod
    def paginate_query_set(request, query_set: QuerySet):
        page_number = 1
    
        if request.GET.get("page_number"):
            page_number = int(request.GET.get("page_number"))
        
        paginator = CustomPaginator(query_set)
        page_range = paginator.get_page_range(page_number)
        current_page = paginator.page(page_number)
        return (current_page, page_range)
