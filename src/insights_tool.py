import os

from .configs.insights_config import INPUT_FOLDER, OUTPUT_FOLDER, INSIGHTS_MESSAGE

from .managers.file_manager import FileManager
from .managers.open_ai_manager import OpenAiManager

class InsightsTool():
    def __init__(self):
        self.open_ai = OpenAiManager()
        self.file_manager = FileManager(INPUT_FOLDER, OUTPUT_FOLDER)
    
    def generate_insights(self):
        file_paths = self.file_manager.get_input_files()
        for fp in file_paths:
            self.generate_insight(fp)

    def generate_insight(self, file_path):
        self.open_ai.upload_file(file_path)
        self.open_ai.create_thread()
        self.open_ai.create_message(INSIGHTS_MESSAGE)
        self.open_ai.run_thread()
        self.open_ai.wait_for_run()
        response = self.open_ai.get_response()
        file_name = os.path.basename(file_path) + '_insights.txt'
        self.file_manager.save_output_file(file_name, response)
        self.open_ai.delete_file(self.open_ai.file_id)