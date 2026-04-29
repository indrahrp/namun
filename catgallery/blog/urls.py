from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('<int:pk>/', views.post_detail, name='detail'),
    path('write/', views.post_write, name='write'),
    path('improve/', views.improve_text, name='improve'),
]
