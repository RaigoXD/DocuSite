from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

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
    # queryset = serializer_class.Meta.model.objects.all()
    # permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['folder_parent', 'type_file__types']
    search_fields = ['name']
    
    def get_queryset(self):
        if self.request.user.rol == 'SU':
            queryset = self.serializer_class.Meta.model.objects.all()
        elif self.request.user.rol == 'AD':
            # Falta modificar
            queryset = self.serializer_class.Meta.model.objects.all()
        else:
            queryset = self.serializer_class.Meta.model.objects.filter(owner__uuid= self.request.user.uuid)        
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FileCreateUpdateSerializer 
        return super().get_serializer_class()


class FileRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = FileRetriveDeleteSerializer
    queryset = serializer_class.Meta.model.objects.all()
    # permission_classes = (IsAuthenticated,)
    lookup_field = 'uuid'
    

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return FileCreateUpdateSerializer 
        return super().get_serializer_class()
    
