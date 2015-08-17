# *-* coding:utf-8 *-*
from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
from .models import Artigo
from .serializers import ArtigoSerializer, UserSerializer

User = get_user_model()

class DefaultMixin(object):
    authetication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )

    paginated_by = 25
    paginated_by_param = 'page_size'
    max_paginate_by = 100

    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

class ArtigoViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Artigo.objects.order_by('data_publicacao')
    serializer_class = ArtigoSerializer
    search_fields = ('titulo',)
    ordering_fields = ('data_publicacao','titulo',)

class UserViewSet(DefaultMixin, viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD)
