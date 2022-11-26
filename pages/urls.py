from django.urls import path
from .views import HomePageView, Homepage

urlpatterns = [
    path('', HomePageView, name="home"),
    path('about/', Homepage.as_view(), name="about")
]
