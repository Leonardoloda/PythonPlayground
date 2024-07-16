from datetime import datetime

from email_client import EmailClient
from repository import Repository

days_of_the_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

repository = Repository(path="files/quotes.txt")
client = EmailClient(path=".env")

today = datetime.now().weekday()

if today == 0:
    quote = repository.get_random_quote()

    subject = f"{days_of_the_week[today]}"
    client.send_email(to="130.testing.auto@gmail.com", subject=subject, body=quote)
    print("Motivational quote sent")
else:
    print("It's not monday, come here another day")
