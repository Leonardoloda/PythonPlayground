from smtplib import SMTP

from dotenv import dotenv_values


class EmailClient:
    """Client to send an email"""

    def __init__(self, path) -> None:
        self.email = ""
        self.password = ""

        self.path = path

        self.initialize()

    def initialize(self):
        """Fetch the credentials for the sender account"""
        config = dotenv_values(self.path)

        email = config.get("EMAIL")
        password = config.get("PASSWORD")

        if not email or not password:
            print("Not a valid email or password")
            exit()

        self.email = email
        self.password = password

    def send_email(self, to, subject, body):
        """Sends email to the target email"""
        with SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            print("credentials:", self.email, self.password)
            connection.login(self.email, self.password)

            connection.sendmail(
                from_addr=self.email,
                to_addrs=to,
                msg=f"Subject:{subject}\n\n{body}",
            )
