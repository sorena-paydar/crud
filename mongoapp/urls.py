from django.urls import path
from . import views

urlpatterns = [
    path('mongo-crud/', views.mongo_crud, name='mongo_crud'),
    path('mongo-crud/<int:pk>/', views.mongo_detail, name='mongo_detail'),
]