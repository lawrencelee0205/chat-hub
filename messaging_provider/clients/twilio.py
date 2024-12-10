from twilio.rest import Client


class TwilioClient:
    def __init__(self, account_sid, auth_token):
        self.client = Client(account_sid, auth_token)

    def send_message(self, from_, to, body):
        message = self.client.messages.create(to=to, from_=from_, body=body)
        return message
