from django.shortcuts import render
from django.views.generic import ListView
from .models import Boook
# Create your views here.

class BookListView(ListView):
    model=Boook
    template_name="book_list.html"
