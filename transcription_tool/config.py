import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
S3_BUCKET = os.getenv('S3_BUCKET')
IAM_USER_ACCESS_KEY = os.getenv('IAM_USER_ACCESS_KEY')
IAM_USER_SECRET_ACCESS_KEY = os.getenv('IAM_USER_SECRET_ACCESS_KEY')

## Project Settings
INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'