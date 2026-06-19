from django.urls import path
from opiniones import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('dejar-opinion/', views.dejar_opinion, name='dejar_opinion'),
    path('ver-opiniones/', views.ver_opiniones, name='ver_opiniones'),
]
