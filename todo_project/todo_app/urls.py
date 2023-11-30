from django.urls import path, include
from rest_framework import routers
from .views import TodoItemViewSet
from .views import display_csrf_token

router = routers.DefaultRouter()
router.register(r'todo', TodoItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', display_csrf_token, name='success_oauth'),
]