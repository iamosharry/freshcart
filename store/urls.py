from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('category', views.CategoryViewSet)

urlpatterns = router.urls
