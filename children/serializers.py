from rest_framework import serializers
from django.contrib.auth.models import User

from children.models import Child

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class ChildListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = ('uuid', 'name')

class ChildDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = ('uuid', 'name', 'age', 'months', 'mother')


