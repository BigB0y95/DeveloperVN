from django.contrib.auth.models import User
from Members.models import Member as member_model

class EmailOrUsernameModelBackend(object):

    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
             kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class Check_Account_member(object):

    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
             kwargs = {'username': username}
        try:
            member = member_model.objects.get(**kwargs)
            if member.check_password(password):
                return member
        except member_model.DoesNotExist:
            return None

    def get_member(self, user_id):
        try:
            return member_model.objects.get(pk=user_id)
        except member_model.DoesNotExist:
            return None