from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileView, AppViewSet, TaskViewSet, CategoryViewSet, SubCategoryViewSet

router = DefaultRouter()
router.register('apps', AppViewSet)
router.register('tasks', TaskViewSet)
router.register('categories', CategoryViewSet)
router.register('subcategories', SubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
