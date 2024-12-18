from django.urls import path, include

from cart.views import CartAddView, ShowCartView, ShowDishView

urlpatterns = [
    path('api/v1/cart_add/<int:pk>/', CartAddView.as_view()),
    path('api/v1/show_cart/', ShowCartView.as_view()),
    path('api/v1/show_dish/', ShowDishView.as_view()),
]
