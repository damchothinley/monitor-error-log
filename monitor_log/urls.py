from django.urls import path
from .views import HomePageView, ErrorView

urlpatterns = [
    path('', HomePageView, name="homepage"),
    path('error/', ErrorView)
]
