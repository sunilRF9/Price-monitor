from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_SID']
account_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, account_token)
client.messages.create(
        to=os.environ['MOB_NO'],
        from_= "+12055798923",
        body="Testing"
)
