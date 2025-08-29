"""
URL patterns for the chatbot app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('clear_chat/', views.clear_chat, name='clear_chat'),
]
