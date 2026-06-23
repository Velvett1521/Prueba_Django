from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from opiniones import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('dejar-opinion/', views.dejar_opinion, name='dejar_opinion'),
    path('opinion-enviada/', views.opinion_enviada, name='opinion_enviada'),
    path('ver-opiniones/', views.ver_opiniones, name='ver_opiniones'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)