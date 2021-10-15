from django.urls import path
#from django.urls.conf import include, path
from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')     #Get URL using include of dajngo
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),              #it charges view as function
    path('', include(router.urls)),                                 #Find all the urls we are using in our routers
]                       