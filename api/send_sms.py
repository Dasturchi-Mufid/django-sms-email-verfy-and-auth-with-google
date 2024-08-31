from twilio.rest import Client
import random
from django.conf import settings

def send_verification_code(phone_number):
    verification_code = random.randint(100000, 999999)
    
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    message = client.messages.create(
        body=f'Your verification code is {verification_code}',
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    
    return verification_code
