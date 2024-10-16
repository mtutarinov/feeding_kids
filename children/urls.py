from django.urls import path, include
from rest_framework.routers import SimpleRouter

from children.views import ChildViewSet

children_router = SimpleRouter()
children_router.register(r'children', ChildViewSet)

urlpatterns = [
    path('api/v1/', include(children_router.urls)),

]