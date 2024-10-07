from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from cart.cart import Cart


class CartAddView(APIView):

    def post(self, request, pk):
        cart = Cart(request)
        cart.add(pk)
        return Response('Товар добавлен в корзину.')


class ShowCart(APIView):

    def get(self, request):
        cart = Cart(request)
        return Response(cart.cart)
