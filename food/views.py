from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from food.models import Dish, Ingredient, DishRating, DishHistory, DishChosen
from food.serializers import IngredientSerializer, DishSerializer, DishRatingSerializer, DishHistorySerializer, \
    DishChosenSerializer
from food.rating_services import rating_services


class ProductViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAuthenticated, )


class DishViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishRatingView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, pk):
        return Response({'response': f'Dish rating {rating_services(pk, request.user)}'})

class DishHistoryView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        history = DishHistory.objects.get(user=request.user)
        return Response({'history': DishHistorySerializer(history, many=True).data})

    def put(self, request, pk):
        history = DishHistory.objects.get(user=request.user)
        history.history.add(pk)
        return Response({'history': DishHistorySerializer(history, many=True).data})

class DishChosenView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        chosen = DishChosen.objects.get(user=request.user)
        return Response({'chosen': DishChosenSerializer(chosen, many=True).data})

    def put(self, request, pk):
        chosen = DishChosen.objects.get(user=request.user)
        chosen.chosen.add(pk)
        return Response({'chosen': DishChosenSerializer(chosen, many=True).data})
