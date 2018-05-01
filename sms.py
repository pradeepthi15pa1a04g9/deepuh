Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
from twilio.rest import Client


account_sid = "ACdab619921d5b29c4e0acf63d72e627e8"
auth_token = "e055aa80f23b7b0ffe781892e0c5b7db"
client = Client(account_sid, auth_token)

message = client.messages.create(
	"+917981136861",
	body="Let's grab lunch at Milliways tomorrow!",
	from_="+13479836248",
    
)

print(message.sid)
