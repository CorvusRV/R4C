from django.urls import path
from .views import RobotsView, AccountView


urlpatterns = [
    path('create/', RobotsView.as_view()),
    path('account/', AccountView.as_view()),
]