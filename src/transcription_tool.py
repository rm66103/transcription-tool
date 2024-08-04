import os
import time

from .configs.transcription_config import IAM_USER_ACCESS_KEY, IAM_USER_SECRET_ACCESS_KEY

from .managers.s3_manager import S3Manager
from .managers.transcribe_manager import TranscribeManager
from .managers.file_manager import FileManager

class TranscriptionTool:
    def __init__(self, input_folder, output_folder, s3_bucket):
        self.output_folder = output_folder
        self.file_manager = FileManager(input_folder, output_folder)
        self.s3_manager = S3Manager(
            s3_bucket,
            IAM_USER_ACCESS_KEY,
            IAM_USER_SECRET_ACCESS_KEY
        )
        self.transcribe_manager = TranscribeManager(
            IAM_USER_ACCESS_KEY,
            IAM_USER_SECRET_ACCESS_KEY
        )

    def process_files(self, speaker_count):
        input_files = self.file_manager.get_input_files()
        for file_path in input_files:

            # Upload the file and start the transcription job
            file_name = os.path.basename(file_path)
            self.s3_manager.upload_file(file_path, file_name)
            self.transcribe_manager.start_transcription(
                file_name, 
                f's3://{self.s3_manager.bucket_name}/{file_name}',
                self.s3_manager.bucket_name,
                speaker_count
            )
            
            # Check transcription status
            while True:
                print("Transcription in progress...")
                status = self.transcribe_manager.get_transcription_status(file_name)
                if status == 'COMPLETED':
                    break
                elif status == 'FAILED':
                    print(f"Transcription failed for {file_name}")
                    return
                time.sleep(5)  # Wait before checking again

            # Download the transcription result
            result_url = self.transcribe_manager.get_transcription_result(file_name)
            job_name = result_url.split('/')[-1]
            output_file_path = f"{self.output_folder}/{job_name}"
            self.s3_manager.download_file(job_name, output_file_path)

            # Cleanup
            self.s3_manager.delete_file(file_name)
            self.s3_manager.delete_file(job_name)