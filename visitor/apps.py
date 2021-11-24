from django.apps import AppConfig


class VisitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visitor'


    # USED FOR THE CREATION OF PROFILES FOR NEW USERS WHEN THEY ARE CREATED
    def ready(self):
        import visitor.signals













