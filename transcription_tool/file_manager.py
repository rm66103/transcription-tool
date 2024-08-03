import os

class FileManager:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def get_input_files(self):
        return [os.path.join(self.input_folder, f) for f in os.listdir(self.input_folder) if os.path.isfile(os.path.join(self.input_folder, f))]

    def save_output_file(self, file_name, content):
        with open(os.path.join(self.output_folder, file_name), 'w') as f:
            f.write(content)