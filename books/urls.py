from django.urls import path
from . import views

urlpatterns = [
    path('addbook/', views.add, name='addbook'),
    path('all/', views.bookview, name='allbooks'),
    path('<int:books_id>', views.detail, name='detail'),
    path('<int:books_id>/download', views.download, name='download'),
    path('search/', views.search, name='search')
]