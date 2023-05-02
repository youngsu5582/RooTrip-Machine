from django.urls import path,include
from .views import connectAPI,connectSQL
urlpatterns = [
    path("connect/",connectAPI),
    path("sql/",connectSQL)
]