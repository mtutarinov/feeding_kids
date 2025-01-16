from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from food.views import (
    AllergenViewSet,
    DishFavouriteView,
    DishHistoryView,
    DishRatingView,
    DishViewSet,
    IngredientViewSet,
)

ingredient_router = SimpleRouter()
ingredient_router.register(r"ingredients", IngredientViewSet)
allergen_router = SimpleRouter()
allergen_router.register(r"allergens", AllergenViewSet)
dish_router = SimpleRouter()
dish_router.register("dishes", DishViewSet)


urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/", include(ingredient_router.urls)),
    path("api/v1/", include(dish_router.urls)),
    path("api/v1/rating/", DishRatingView.as_view()),
    path("api/v1/history/", DishHistoryView.as_view()),
    path("api/v1/favourite/", DishFavouriteView.as_view()),
    path("api/v1/child/<int:child_id>/", include(allergen_router.urls)),
]
