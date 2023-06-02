from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import UserCreateUpdateSerializer, UserListRetrieveDestroySerializer

from rest_framework.permissions import IsAuthenticated


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserCreateUpdateSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserListRetrieveDestroySerializer
        return super().get_serializer_class()


class UserListRetrieveDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserListRetrieveDestroySerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = (IsAuthenticated,)
    lookup_field = 'uuid'
