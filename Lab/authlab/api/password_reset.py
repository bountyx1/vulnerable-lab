import jwt
from .models import User
from django.conf import settings
from datetime import datetime, timedelta
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class UserReset:
	def generate_token(self,email):
		email=email.lower()
		try:
			user=User.objects.get(email=email)
			timestamp = datetime.now() + timedelta(hours=1)
			token = jwt.encode({
			'email':user.email,
			'exp':int(timestamp.strftime('%s'))
			},settings.SECRET_KEY, algorithm='HS256')
			self.send_mail(email,token)
			return True
		except User.DoesNotExist:
			return False

	def send_mail(self,email,token):
		report=open("/home/chitoge/password-reset.html").read()
		report = report.replace("{email}",email)
		report = report.replace("{ipaddress}","127.0.0.1")
		#Convert base64 bytes to string
		report = report.replace("{token}","http://localhost:8000/api/reset/token?token="+token.decode('UTF-8'))
                # Note for future change key here to env variable
		try:    
			sg = SendGridAPIClient('your sendgrid key')
			response = sg.send(Mail(from_email='no-reply@chitoge.com',to_emails=email,subject='Password Reset ',html_content=report))
			print(response)
		except Exception as e:
			return "error sending mail"

	def validate_token(self,token):
		payload=jwt.decode(token,settings.SECRET_KEY)
		timestamp = int(datetime.now().strftime('%s'))
		if payload["exp"] <= timestamp:
			return {"status":"expired"}
		else:
			return {"status":"valid","email":payload["email"]}
