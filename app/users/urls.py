from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.UserViewSet, basename='search')
# router.register('register/', views.register, basename='register'),
# router.register('login/', views.custom_login, basename='login'),
# router.register('logout/', views.custom_login, basename='logout'),



# urlpatterns = [
#     path('register/', views.register, name='register'),
#     path('login/', views.custom_login, name='login'),
#     path('logout/', views.custom_login, name='logout'),

# ]


urlpatterns = [
    path('', include(router.urls)),
]