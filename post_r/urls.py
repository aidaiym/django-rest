from django.urls import path
from .views import *

urlpatterns = [
    path('posts', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>', DetailView.as_view(), name='post_detail'),
    path('categories/', CategoryList.as_view(), name='category_list')
]