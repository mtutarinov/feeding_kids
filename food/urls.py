from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from food.models import DishHistory
from food.views import IngredientViewSet, DishViewSet

ingredient_router = SimpleRouter()
ingredient_router.register(r'ingredients', IngredientViewSet)
dish_router = SimpleRouter()
dish_router.register('dishes', DishViewSet)
from food.views import DishRatingView, DishHistoryView, DishFavouriteView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include(ingredient_router.urls)),
    path('api/v1/', include(dish_router.urls)),
    path('api/v1/rating/', DishRatingView.as_view()),
    path('api/v1/history/', DishHistoryView.as_view()),
    path('api/v1/favourite/', DishFavouriteView.as_view()),
]
