from django.contrib.auth import get_user_model
from rest_framework import viewsets

from api.filters import UserFilter
from api.permissions import IsSelf
from api.serializers import (UserListSerializer,
                             UserRetrieveSerializer,
                             UserCreateSerializer,
                             UserUpdateSerializer,
                             UserPartialUpdateSerializer)

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    filter_class = UserFilter
    permission_classes = (IsSelf,)
    search_fields = ('fullname',)

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        if self.action == 'retrieve':
            return UserRetrieveSerializer
        if self.action == 'create':
            return UserCreateSerializer
        if self.action == 'update':
            return UserUpdateSerializer
        if self.action == 'partial_update':
            return UserPartialUpdateSerializer
        return UserListSerializer
