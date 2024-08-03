import os
from transcription_tool.transcription_tool import TranscriptionTool
from dotenv import load_dotenv

from transcription_tool.config import S3_BUCKET, INPUT_FOLDER, OUTPUT_FOLDER


if __name__ == '__main__':
    tool = TranscriptionTool(INPUT_FOLDER, OUTPUT_FOLDER, S3_BUCKET)
    tool.process_files()