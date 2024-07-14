from datetime import datetime

from template_manager import TemplateManager
from email_client import EmailClient
from repository import Repository

from constants import *


client = EmailClient(path=CREDENTIALS_PATH)

file_manager = TemplateManager(templates_path=TEMPLATES_PATH)
birthday_repo = Repository(path=BIRTHDAYS_PATH)

birthdays = birthday_repo.active_birthdays(datetime.today())


for _, birthday in birthdays.iterrows():
    template = file_manager.get_random_template()

    personalized_template = template.replace(NAME_PATTERN, birthday["name"])

    client.send_email(birthday.email, "Happy Birthday", personalized_template)

    print(f"Email sent to {birthday.email}")

print("All birthdays have been checked, exiting the program...")
