from django.urls import path

from cart.views import CartView, ShowDishView

urlpatterns = [
    path("api/v1/cart/", CartView.as_view()),
    path("api/v1/show_dishes/", ShowDishView.as_view()),
]
