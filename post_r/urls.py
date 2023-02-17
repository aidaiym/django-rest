from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'posts', PostListView)
router.register(r'categories', CategoryListView)

urlpatterns = [
    path('', include(router.urls)),
]