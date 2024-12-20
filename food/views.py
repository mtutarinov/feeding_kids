from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from food.filters import DishTypeFilter
from food.models import Dish, Ingredient
from food.serializers import (
    DishFavouriteSerializer,
    DishHistorySerializer,
    DishSerializer,
    IngredientSerializer,
)
from food.services.history_favorite import FavouriteManager, HistoryManager
from food.services.rating import rate_dish


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    # permission_classes = (IsAuthenticated,)


class DishViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filterset_class = DishTypeFilter


class DishRatingView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response(
            {"response": f'Dish rating {rate_dish(request.data["id"], request.user)}'}
        )


class DishHistoryView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        history = HistoryManager.get(user=request.user)
        return Response({"history": DishHistorySerializer(history, many=True).data})

    def post(self, request):
        HistoryManager.add(dish_id=request.data["id"], user=request.user)
        history = HistoryManager.get(user=request.user)
        return Response({"history": DishHistorySerializer(history, many=True).data})

    def delete(self, request):
        HistoryManager.delete(user=request.user, dish_id=request.data["id"])
        history = HistoryManager.get(user=request.user)
        return Response({"history": DishHistorySerializer(history, many=True).data})


class DishFavouriteView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        favourite = FavouriteManager.get(user=request.user)
        return Response(
            {"favourite": DishFavouriteSerializer(favourite, many=True).data}
        )

    def post(self, request):
        FavouriteManager.add(dish_id=request.data["id"], user=request.user)
        favourite = FavouriteManager.get(request.user)
        return Response(
            {"favourite": DishFavouriteSerializer(favourite, many=True).data}
        )

    def delete(self, request):
        FavouriteManager.delete(user=request.user, dish_id=request.data["id"])
        favourite = FavouriteManager.get(request.user)
        return Response(
            {"favourite": DishFavouriteSerializer(favourite, many=True).data}
        )
