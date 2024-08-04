import os
import argparse
from dotenv import load_dotenv

from src.configs.transcription_config import S3_BUCKET, INPUT_FOLDER, OUTPUT_FOLDER
from src.transcription_tool import TranscriptionTool

def main(speaker_count):
    tool = TranscriptionTool(INPUT_FOLDER, OUTPUT_FOLDER, S3_BUCKET)
    tool.process_files(speaker_count)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--speaker_count', type=int, default=1 , help='Number of speakers in input files.')

    args = parser.parse_args()

    main(args.speaker_count)