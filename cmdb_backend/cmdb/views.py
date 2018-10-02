from django.contrib.auth.models import User, Group
from cmdb.models import Application, Bu, Product, Host
from rest_framework import viewsets, filters
from cmdb.serializers import UserSerializer, GroupSerializer, ApplicationSerializer, BuSerializer, ProductSerializer, HostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Applications to be viewed or edited.
    """
    queryset = Bu.objects.all()
    serializer_class = BuSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'bu')

class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Applications to be viewed or edited.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'product')

class HostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Hosts to be viewed or edited.
    """
    queryset = Host.objects.all()
    serializer_class = HostSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'ip', 'application')




