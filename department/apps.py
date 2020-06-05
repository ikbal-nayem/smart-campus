from django.apps import AppConfig


class DepartmentConfig(AppConfig):
    name = 'department'

    def ready(self):
        import department.signals
