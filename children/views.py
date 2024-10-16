from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from children.serializers import ChildListSerializer, ChildDetailSerializer
from children.models import Child


class ChildViewSet(ModelViewSet):
    queryset = Child.objects.all()
    permission_classes = (IsAuthenticated, )
    lookup_field = 'uuid'

    def get_queryset(self):
        return super().get_queryset().only('uuid', 'name')


    def get_serializer_class(self):
        if self.action == 'list':
            return ChildListSerializer
        return ChildDetailSerializer
