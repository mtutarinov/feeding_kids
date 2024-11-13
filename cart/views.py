from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cart.cart import Cart
from food.models import Ingredient, Dish
from food.serializers import ShowDishSerializer


class CartAddView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        cart = Cart(request)
        cart.add(pk)
        return Response('Товар добавлен в корзину.')


class ShowCartView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        cart = Cart(request)
        return Response(cart.cart)


class ShowDishView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        cart = Cart(request)
        ingredients_ids = cart.cart
        dish = Dish.objects.filter(ingredients__id__in=ingredients_ids).distinct()
        return Response({'dishes': ShowDishSerializer(dish, many=True).data})
