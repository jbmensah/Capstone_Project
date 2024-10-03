import dataclasses
import datetime
import jwt
from typing import TYPE_CHECKING
from django.conf import settings


from . models import User


if TYPE_CHECKING:
	from user.models import User

@dataclasses.dataclass
class UserDataClass:
	first_name: str
	last_name: str
	email: str
	password: str = None
	id: int = None

	@classmethod
	def from_instance(cls, user: "User") -> "UserDataClass":
		return cls(
			id = user.id,
			first_name = user.first_name,
			last_name = user.last_name,
			email = user.email
		)
	
def create_user(user_dc: "UserDataClass") -> "UserDataClass":
	instance = User(
		first_name = user_dc.first_name,
		last_name = user_dc.last_name,
		email = user_dc.email		
	)
	if user_dc.password is not None:
		instance.set_password(user_dc.password)
	instance.save()

	return UserDataClass.from_instance(instance)

def user_email_selector(email: str) -> "UserDataClass":
	user = User.objects.filter(email=email).first()
	 
	return user

def create_toke(user_id: int) -> str:
	payload = dict(
		id = user_id,
		exp = datetime.datetime.utcnow() + datetime.timedelta(hours=24),
		iat = datetime.datetime.utcnow()
	)
	token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")

	return token