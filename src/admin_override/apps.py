from django.apps import AppConfig


class AdminOverrideConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_override'
