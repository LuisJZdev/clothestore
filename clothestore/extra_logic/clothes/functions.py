from django.db.models import QuerySet

def make_pagination(queryset: QuerySet, page_number: int, pagination_number: int):
    assert page_number != 0, "you can't paginate from zero"
    return queryset[pagination_number*(page_number-1):(pagination_number*(page_number-1)+pagination_number)]

def get_pagination_numbers(queryset: QuerySet, pagination_number: int):
    final_number = 0

    for i in range(1, len(queryset)+1):
        if make_pagination(queryset, i, pagination_number):
            final_number += 1

    return final_number