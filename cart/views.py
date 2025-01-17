from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.cart import Cart
from cart.dish_constructor import DishConstructor
from food.models import Allergen
from food.serializers import ShowDishSerializer


class CartView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        cart = Cart(request)
        cart.add(request.data["ingredients_id"])
        return Response("Ингредиент добавлен в корзину.")

    def get(self, request):
        cart = Cart(request)
        return Response(cart.cart)

    def delete(self, request):
        cart = Cart(request)
        cart.remove(request.data["ingredients_id"])
        return Response("Ингредиент удален из корзины.")


class DishConstructorView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        cart = Cart(request)
        available_ids = cart.cart
        allergens = Allergen.objects.filter(child=request.data["child"]).values(
            "ingredient_id"
        )
        allergens_ids = [allergen["ingredient_id"] for allergen in allergens]
        result = DishConstructor.get(available_ids, allergens_ids)
        return Response({"dishes": ShowDishSerializer(result, many=True).data})
