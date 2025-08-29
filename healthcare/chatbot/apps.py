"""
Chatbot app configuration.
"""
from django.apps import AppConfig


class ChatbotConfig(AppConfig):
    """Configuration for the chatbot app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'healthcare.chatbot'
