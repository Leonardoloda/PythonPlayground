from os import getenv

from dotenv import load_dotenv

from google_bot import GoogleBot
from website_client import WebsiteClient
from zillow_bot import ZillowBot

# Load environment variables from the .env file
load_dotenv()

# Get the Google Form URL and Zillow URL from environment variables
GOOGLE_FORM_URL = getenv('GOOGLE_FORM_URL')
ZILLOW_URL = getenv('ZILLOW_URL')

# Fetch the webpage content from the Zillow URL
print("Fetching Zillow page content...")
page = WebsiteClient.fetch_page(url=ZILLOW_URL)

# Initialize the ZillowBot with the fetched page content
print("Initializing ZillowBot...")
zillow_bot = ZillowBot(page)

# Initialize the GoogleBot with the Google Form URL
print("Initializing GoogleBot...")
google_bot = GoogleBot(url=GOOGLE_FORM_URL)

# Fetch the list of properties from the Zillow page
print("Fetching properties from Zillow...")
properties = zillow_bot.fetch_properties()
print(f"Found {len(properties)} properties.")

# Loop through each property and fill out the Google Form
for index, property in enumerate(properties, start=1):
    print(f"Processing property {index} of {len(properties)}: {property}")
    google_bot.load_page()  # Load the Google Form page
    google_bot.fill_form(property)  # Fill the form with property details
    google_bot.close_page()  # Close the tab
    print("Form submitted successfully.")

print("All properties have been processed and submitted.")
