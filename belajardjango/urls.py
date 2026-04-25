from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('biodata/', views.biodata),
    path('blog/', views.blog),
    path('kontak/', views.kontak),
]