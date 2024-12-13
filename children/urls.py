from django.urls import path, include
from rest_framework.routers import SimpleRouter

from children.views import ChildViewSet, UserViewSet

user_router = SimpleRouter()
user_router.register(r'user', UserViewSet)
children_router = SimpleRouter()
children_router.register(r'children', ChildViewSet)

urlpatterns = [
    path('api/v1/', include(children_router.urls)),
    path('api/v1/', include(user_router.urls)),
]
