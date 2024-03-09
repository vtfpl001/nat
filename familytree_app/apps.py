#/home/keyurjoshi/familytree_project/familytree_app/apps.py
from django.apps import AppConfig

class FamilytreeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'familytree_app'

    def ready(self):
        # Your code to execute when the app is ready
        # For example, you can import and register your context processors here
        from familytree_app import context_processors
