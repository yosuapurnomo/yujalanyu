from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class email(ModelBackend):
	def authenticate(self, request, username=None, password=None, **kwargs):
		UserModel = get_user_model()
		try:
			user = UserModel.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username))
		except UserModel.DoesNotExist:
			return None
		else:
			if user.check_password(password):
				return user
		return None

	def get_user(self, user_id):
		UserModel = get_user_model()
		try:
			user = UserModel.objects.get(pk=user_id)
		except UserModel.DoesNotExist:
			return None

		return user if self.user_can_authenticate(user) else None