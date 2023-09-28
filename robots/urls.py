from django.urls import path
from .views import RobotsView


urlpatterns = [
    path('create/', RobotsView.as_view()),
]