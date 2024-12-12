from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from food.models import Dish, Ingredient, DishHistory, DishFavourite
from food.serializers import IngredientSerializer, DishSerializer, DishHistorySerializer, DishFavouriteSerializer
from food.rating_services import rate_dish
from food.history_favorite_services import ActionManager


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAuthenticated,)


class DishViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishRatingView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response({'response': f'Dish rating {rate_dish(request.data["id"], request.user)}'})


class DishHistoryView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        history = ActionManager.get(DishHistory, request.user)
        return Response({'history': DishHistorySerializer(history, many=True).data})

    def post(self, request):
        ActionManager.add(DishHistory,dish_id=request.data['id'], user=request.user)
        history = ActionManager.get(DishHistory, request.user)
        return Response({'history': DishHistorySerializer(history, many=True).data})

    def delete(self, request):
        ActionManager.delete(DishHistory, user=request.user, dish_id=request.data['id'])
        history = ActionManager.get(DishHistory, request.user)
        return Response({'history': DishHistorySerializer(history, many=True).data})


class DishFavourView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        history = ActionManager.get(DishFavourite, request.user)
        return Response({'history': DishFavouriteSerializer(history, many=True).data})

    def post(self, request):
        ActionManager.add(DishFavourite, dish_id=request.data['id'], user=request.user)
        history = ActionManager.get(DishFavourite, request.user)
        return Response({'history': DishFavouriteSerializer(history, many=True).data})

    def delete(self, request):
        ActionManager.delete(DishFavourite, user=request.user, dish_id=request.data['id'])
        history = ActionManager.get(DishFavourite, request.user)
        return Response({'history': DishFavouriteSerializer(history, many=True).data})
