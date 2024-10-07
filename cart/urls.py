from django.urls import path, include

from cart.views import CartAddView, ShowCart

urlpatterns = [
    path('api/v1/cart_add/<int:pk>/', CartAddView.as_view()),
    path('api/v1/show_cart/', ShowCart.as_view()),
]
