from twilio.rest import Client 
import os

account_sid = os.environ("account_sid")
auth_token = os.environ("auth_token")
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hello Everyone, Nice to meet you.",
                    from_='+17066903771',
                    to='+91 9810117777'
                )

print(message.sid)