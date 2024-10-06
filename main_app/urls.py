from django.urls import path, include
from rest_framework.routers import SimpleRouter

from main_app.views import ProductViewSet, DishViewSet

product_router = SimpleRouter()
product_router.register(r'products', ProductViewSet)
dish_router = SimpleRouter()
dish_router.register('dishes', DishViewSet)

urlpatterns = [
    path('api/v1/', include(product_router.urls)),
    path('api/v1/', include(dish_router.urls))
]
