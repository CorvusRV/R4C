from django.urls import path
from .views import RobotsView,ReportView


urlpatterns = [
    path('create/', RobotsView.as_view()),
    path('report/', ReportView.as_view()),
]