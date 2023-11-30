from django.contrib import admin
from django.urls import path, include, re_path
from social_django import urls as social_django_urls
from rest_framework import routers  # Import routers module


from todo_app.views import TodoItemViewSet  # Import the TodoItemViewSet

router = routers.DefaultRouter()
router.register(r'todo', TodoItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo_app.urls')),
    path('login/', include('todo_app.urls')),
    re_path(r'^auth/', include('social_django.urls', namespace='social')),
    path('api/', include(router.urls)),  # Include the TodoItemViewSet URLs
    path('accounts/', include('todo_app.urls')),

]
