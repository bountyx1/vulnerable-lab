from api.models import User
from django.conf import settings
import jwt


class Authandler:
	def validate(self,token):
		payload=jwt.decode(token,settings.SECRET_KEY)
		return payload["user"]