from django.urls import path
from .views import BookListView

urlpatters=[
    path('',BookListView.as_view(),name='home')
]