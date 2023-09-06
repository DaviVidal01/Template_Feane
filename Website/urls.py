from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('menu/', views.menu, name="menu"),
    path('livro/', views.livro, name="livro")
]
