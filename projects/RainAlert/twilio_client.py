from twilio.rest import Client


class TwilioClient:
    def __init__(self, account_sid: str, auth_token: str) -> None:
        self.client = Client(account_sid, auth_token)

    def send_message(self, to: str, body: str, from_: str = "+15005550006") -> None:
        return self.client.api.account.messages.create(to=to, body=body, from_=from_)
