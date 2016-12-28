from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class CustomBackend(ModelBackend):
    def authenticate(self, *args, **kwargs):
        if kwargs:
            telephone = kwargs.pop("telephone", None)
            if telephone:
                password = kwargs.pop("password", None)
                try:
                    user = User.objects.get(telephone=telephone)
                    if user.check_password(password):
                        return user
                except User.DoesNotExist:
                    return None
        return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user

        except User.DoesNotExist:
            return None
