from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from children.serializers import ChildListSerializer, ChildDetailSerializer, UserSerializer
from children.models import Child
from food.models import DishFavourite, DishHistory

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        DishHistory.objects.create(user=request.user)
        DishFavourite.objects.create(user=request.user)
        super().create(request, *args, **kwargs)



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
