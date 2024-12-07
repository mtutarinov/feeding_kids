from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from food.models import Dish, Ingredient, DishRating
from food.serializers import IngredientSerializer, DishSerializer, DishRatingSerializer
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