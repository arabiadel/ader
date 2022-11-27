from django.urls import path
from .views import PostHomeView

urlpatterns = [
    path('', PostHomeView.as_view(), name="home"),
]
