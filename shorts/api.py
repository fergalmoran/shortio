from rest_framework import generics, permissions

from .serializers import UserSerializer, UrlSerializer
from .models import User, Url
from shorts.permissions import UrlAuthorCanEditPermission


class UserList(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    permissions_classess = [
        permissions.AllowAny
    ]


class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    lookup_field = 'username'


class UrlMixin(object):
    model = Url
    serializer_class = UrlSerializer
    permission_classes = [
        UrlAuthorCanEditPermission
    ]

class UrlList(UrlMixin, generics.ListCreateAPIView):
    pass

class UrlDetail(UrlMixin, generics.RetrieveUpdateDestroyAPIView):
    pass

class UserUrlList(generics.ListAPIView):
    model = Url
    serializer_class = UrlSerializer

    def get_queryset(self):
        queryset = super(UserUrlList, self).get_queryset()
        return queryset.filter(user__username=self.kwargs.get('username'))
