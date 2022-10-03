from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePagesView, name='home'),
    path('agent/', views.AgentPagesView, name='agent'),
    path('properties/', views.PropertiesPagesView, name='properties'),
    path('contact/', views.ContactPagesView, name='contact'),
    path('properties/<int:pk>/', views.PropertiesSinglePagesView, name='propertie_single'),
]
