from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipie import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingedients', views.IngredientViewSet)

app_name = 'recipie'

urlpatterns = [
    path('', include(router.urls))
]
