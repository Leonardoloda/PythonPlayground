from smtplib import SMTP


class EmailClient:
    """Client to send an email"""

    def __init__(self, email: str, password: str) -> None:
        self._email = email
        self._password = password

    def send_email(self, to, subject, body):
        """Sends email to the target email"""
        with SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(self._email, self._password)

            connection.sendmail(
                from_addr=self._email,
                to_addrs=to,
                msg=f"Subject:{subject}\n\n{body}",
            )
