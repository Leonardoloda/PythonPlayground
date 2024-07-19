from twilio.rest import Client
from twilio.rest.api.v2010.account.message import MessageInstance


class TwilioClient:
    def __init__(self, account_sid: str, auth_token: str) -> None:
        self._client = Client(account_sid, auth_token)

    def send_message(self, to: str, body: str, from_: str = "+15005550006") -> MessageInstance:
        return self._client.api.account.messages.create(to=to, body=body, from_=from_)

    def send_whatsapp_message(self, to: str, body: str) -> MessageInstance:
        return self._client.messages.create(
            from_='whatsapp:+14155238886',
            body=body,
            to=to
        )
