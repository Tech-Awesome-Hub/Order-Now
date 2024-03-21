
from django.shortcuts import render
from .shop import shop


def search_view(request):
    query = request.GET.get('search_query')
    master_query = request.GET.get('search__query') 

    if not query:
        query = None
    if not master_query:
        master_query = None

    request.session['search_query'] = query
    request.session['search__query'] = master_query
   
    return shop(request)
