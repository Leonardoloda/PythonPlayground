from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

load_dotenv()

document = PdfReader('assets/offer.pdf')

content = ""
for page in document.pages:
    content += page.extract_text()

content = content.strip()

client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=content
)

response.stream_to_file(speech_file_path)
