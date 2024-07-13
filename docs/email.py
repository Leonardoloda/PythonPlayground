import smtplib

# To keep the credentialas secure use a configuration file
from dotenv import dotenv_values

# Read it from the filesystem
config = dotenv_values("files/credentials.env")  # take environment variables

# Now yo ucan get your value
EMAIL = config.get("EMAIL")
PASSWORD = config.get("PASSWORD")

if not EMAIL or not PASSWORD:
    raise ValueError("Either EMAIL or PASSWORD must be set")

# Emails can be sent by creating a new connection
connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(EMAIL, PASSWORD)

# Both body and subject are kept in the msg
connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="Subject: Hello World\n\n Body:Hello world", )

connection.close()

print("Email sent!")

# Emails can also be sent using the with and we can avoid havint to close the connection
with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(EMAIL, PASSWORD)

    connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL)
