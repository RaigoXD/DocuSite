from django.urls import path
from .view import UserListCreateView, UserListRetrieveUpdateDestroyView


urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='users api'),
    path('users/<uuid:uuid>/', UserListRetrieveUpdateDestroyView.as_view(), name='users api'),
]
