from django.urls import path
from .view import (
    TypeFileListView,
    FileListCreateView,
    FileRetrieveUpdateDestroyView
)

urlpatterns = [
    path('types/', TypeFileListView.as_view(), name="List Types of File"),
    path('files/', FileListCreateView.as_view(), name="File API"),
    path('files/<uuid:uuid>', FileRetrieveUpdateDestroyView.as_view(), name="File API")
]