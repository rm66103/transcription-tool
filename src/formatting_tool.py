import json
import os

from .managers.file_manager import FileManager
from .managers.open_ai_manager import OpenAiManager

from .configs.formatting_config import INPUT_FOLDER, OUTPUT_FOLDER

class FormattingTool():
    def __init__(self):
        self.open_ai_manager = OpenAiManager()
        self.file_manager = FileManager(
            INPUT_FOLDER,
            OUTPUT_FOLDER
        )

    def format_transcripts(self):
        input_files = self.file_manager.get_input_files()

        for fp in input_files:
            # Read the JSON file
            with open(fp, 'r') as f:
                data = json.load(f)

            results = data["results"]

            # Save the extracted data to a new text file
            audio_segments_fp = f"{fp.split('/')[-1].replace('.json', '_audio_segments.txt')}"
            formatted_segments = []
            for segment in results["audio_segments"]:
                if 'speaker_label' in segment:
                    formatted_segments.append(f"{segment['speaker_label']} | {segment['transcript']}")
                else:
                    formatted_segments.append(segment['transcript'])
            self.file_manager.save_output_file(audio_segments_fp, "\n".join(formatted_segments))