from rest_framework import serializers

from children.models import Child

class ChildListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = ('uuid', 'name')

class ChildDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = ('uuid', 'name', 'age', 'months', 'mother')


