from django.urls import path
from . import views

app_name = 'cats'

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<int:pk>/', views.cat_detail, name='detail'),
]
