from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('publications/', views.PublicationListCreateAPIView.as_view()),
    path('publications/<int:pk>/', views.PublicationRetrieveUpdateDestroyAPIView.as_view()),
]
