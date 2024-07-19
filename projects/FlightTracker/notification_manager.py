from mail_client import EmailClient
from twilio_client import TwilioClient


class NotificationManager:
    TEMPLATE = "Price alert, the price from [FROM] to [TO] is now at $[PRICE]"

    def __init__(self, mail_client: EmailClient, message_client: TwilioClient, users: list) -> None:
        self._mail_client = mail_client
        self._message_client = message_client

        self._users = users

    def build_message(self, from_: str, to: str, price: str) -> str:
        message_with_from = self.TEMPLATE.replace("[FROM]", from_)
        message_with_to = message_with_from.replace("[TO]", to)
        message = message_with_to.replace("[PRICE]", price)

        return message

    def trigger_price_alert(self, from_: str, to: str, price: str) -> bool:
        message = self.build_message(from_, to, price)

        for user in self._users:
            self._mail_client.send_email(to=user["email"], subject="Flight Alert", body=message)

        self._message_client.send_whatsapp_message(to="whatsapp:+573193189542", body=message)
