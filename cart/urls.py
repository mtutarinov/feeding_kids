from django.urls import path

from cart.views import CartView, DishConstructorView

urlpatterns = [
    path("api/v1/cart/", CartView.as_view()),
    path("api/v1/dish_constructor/", DishConstructorView.as_view()),
]
