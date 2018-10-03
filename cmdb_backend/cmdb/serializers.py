from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Application, Bu, Product, Host


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups','password')
        ordering = ['id']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
        ordering = ['id']


class BuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bu
        fields = '__all__'
        ordering = ['id']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        ordering = ['id']

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'
        ordering = ['id']






class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'
        ordering = ['id']