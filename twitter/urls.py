from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:twitter_id>/', views.delete, name='delete'),
    path('update/<int:twitter_id>/', views.update, name='update'),
]

