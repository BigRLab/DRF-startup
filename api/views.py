from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet

from api.filters import UserFilter
from api.serializers import *

User = get_user_model()


class BaseModelViewSet(viewsets.ModelViewSet):
    def __init__(self, **kwargs):
        GenericViewSet.__init__(self, **kwargs)
        self.name = self.__class__.__name__.replace('ViewSet', '')

    def get_serializer_class(self):
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

    class Meta:
        abstract = True


class UserViewSet(BaseModelViewSet):
    queryset = User.objects.all()
    filter_class = UserFilter
    # permission_classes = (IsSelf,)
    search_fields = ('fullname',)
