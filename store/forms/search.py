# forms.py
from django import forms

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=255, required=False)
