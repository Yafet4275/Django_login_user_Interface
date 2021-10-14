from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloAPIview.as_view()),              #it charges view as function
]