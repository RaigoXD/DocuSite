from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from .serializer import (
    TypeFileSerializer,
    FileCreateUpdateSerializer,
    FileRetriveDeleteSerializer,
    FileListSerializer
)


class TypeFileListView(ListAPIView):
    serializer_class = TypeFileSerializer
    queryset = serializer_class.Meta.model.objects.all()
    filter_backends = [DjangoFilterBackend]
    permission_classes = (IsAuthenticated, )
    filterset_fields = ['is_active']


class FileListCreateView(ListCreateAPIView):
    serializer_class = FileListSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FileCreateUpdateSerializer 
        return super().get_serializer_class()


class FileRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = FileRetriveDeleteSerializer
    queryset = serializer_class.Meta.model.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return FileCreateUpdateSerializer 
        return super().get_serializer_class()
    
