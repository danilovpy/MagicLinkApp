# from .models import User
# from django.contrib.auth.backends import ModelBackend
#
#
#
# class UserBackend(ModelBackend):
#
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             token = kwargs['token']
#             user = User.objects.get(self, token=token)
#             return user
#         except User.DoesNotExist:
#             return None
#
