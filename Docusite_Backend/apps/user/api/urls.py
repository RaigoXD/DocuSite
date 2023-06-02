from django.urls import path
from .view import UserListCreateView, UserListRetrieveDestroyView


urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='users api'),
    path('users/<uuid:uuid>/', UserListRetrieveDestroyView.as_view(), name='users api'),
]
