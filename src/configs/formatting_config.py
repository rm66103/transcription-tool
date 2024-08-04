import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')
OPEN_AI_ASSISTANT_ID = os.getenv('OPEN_AI_ASSISTANT_ID')

INPUT_FOLDER = 'output/raw_transcripts'
OUTPUT_FOLDER = 'output/formatted_transcripts'
