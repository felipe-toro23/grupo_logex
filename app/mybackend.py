from django.contrib.auth.backends import BaseBackend
from .models import Usuarios

class MyBackend(BaseBackend):
    def authenticate(self, username=None, password=None):
        user = Usuarios.objects.get(rut_cli=rut_cli)
        if not user is None:
            if user.password == password:
                return user
        return None

    def get_user(self, user_id):
        try:
            return Usuarios.objects.get(pk=user_id)
        except Exception:
            return None