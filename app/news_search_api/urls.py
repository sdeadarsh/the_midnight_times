from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('search', views.SearchKeywordViewSet, basename='search')
router.register('results', views.SearchResultViewSet, basename='results')

# urlpatterns = [
#     path('search', views.SearchKeywordViewSet, name='search'),
#     path('results/', views.results, name='results'),
# ]

urlpatterns = [
    path('', include(router.urls)),
]