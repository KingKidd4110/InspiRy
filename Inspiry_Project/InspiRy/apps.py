from django.apps import AppConfig


class InspiryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'InspiRy'
    
    def ready(self):
        import InspiRy.signals
