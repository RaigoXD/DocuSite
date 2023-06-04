from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import UserCreateUpdateSerializer, UserListRetrieveDestroySerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserCreateUpdateSerializer
    queryset = serializer_class.Meta.model.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = (IsAuthenticated,)
    filterset_fields = ['rol']  # Filter using QueryParam
    search_fields = ['username', 'email'] # Search using QueryParam 

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListRetrieveDestroySerializer
        return super().get_serializer_class()


class UserListRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserListRetrieveDestroySerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = 'uuid'
