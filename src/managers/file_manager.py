import os

class FileManager:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def get_files_in_directory(self, directory):
        files = []
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                files.append(os.path.join(directory, file))
        return files

    def get_input_files(self):
        return self.get_files_in_directory(self.input_folder)

    def save_output_file(self, file_name, content):
        with open(os.path.join(self.output_folder, file_name), 'w') as f:
            f.write(content)