
from .shop import shop


def filter_view(request):
    query = request.GET.get('filter_query')
    # master_query = request.GET.get('search__query') 

    if not query:
        query = None
    # if not master_query:
    #     master_query = None

    request.session['filter_query'] = query
    # request.session['search__query'] = master_query
   
    return shop(request)
