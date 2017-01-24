from rest_framework import filters
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet

from api.permissions import CustomObjectPermissions, IsSelf
from api.serializers import *
from api.filters import *

User = get_user_model()


class BaseModelViewSet(viewsets.ModelViewSet):
    def __init__(self, **kwargs):
        GenericViewSet.__init__(self, **kwargs)
        self.name = self.__class__.__name__.replace('ViewSet', '')
        self.filter_class = eval("{}Filter".format(self.name))

    def get_serializer_class(self):
        try:
            if self.action == 'list':
                return eval("{}ListSerializer".format(self.name))
            if self.action == 'retrieve':
                return eval("{}RetrieveSerializer".format(self.name))
            if self.action == 'create':
                return eval("{}CreateSerializer".format(self.name))
            if self.action == 'update':
                return eval("{}UpdateSerializer".format(self.name))
            if self.action == 'partial_update':
                return eval("{}PartialUpdateSerializer".format(self.name))
            return eval("{}ListSerializer".format(self.name))
        finally:
            return eval("{}ListSerializer".format(self.name))

    class Meta:
        abstract = True


class UserViewSet(BaseModelViewSet):
    queryset = User.objects.all()
    permission_classes = [CustomObjectPermissions, ]
    search_fields = ('fullname',)
