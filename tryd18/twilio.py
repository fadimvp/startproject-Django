from twilio.rest import TwilioRestClient
account_sid ="ACf0c8c44da31cc097efc7b6ca03d1bd88"
auth_token="ad538d89c13a261fb37141ea59d8ca74"
client =TwilioRestClient(account_sid,auth_token)
message =client.sms.message.create(
    body ="please ? ! i love you < 3",
    to="+13023375057",
    from_="00201122216124")
print message.sid