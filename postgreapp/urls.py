from django.urls import path
from . import views

urlpatterns = [
    path('postgre-crud/', views.postgres_crud, name='postgres-crud'),
    path('postgre-crud/<int:pk>/', views.postgres_detail, name='postgres-detail'),
]
