from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('<str:nome>/', views.detalhes_post, name='detalhes_post'),
]