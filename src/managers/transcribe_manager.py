import boto3

class TranscribeManager:
    def __init__(self, aws_access_key_id, aws_secret_access_key):
        self.transcribe = boto3.client(
            'transcribe',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    def start_transcription(self, job_name, file_uri, output_bucket, speaker_count):
        settings = {}

        if speaker_count > 1:
            settings['ShowSpeakerLabels'] = True
            settings['MaxSpeakerLabels'] = speaker_count

        try:
            response = self.transcribe.start_transcription_job(
                TranscriptionJobName=job_name,
                Media={'MediaFileUri': file_uri},
                OutputBucketName=output_bucket,
                LanguageCode='en-US',
                Settings=settings
            )
            return response
        except self.transcribe.exceptions.ConflictException as e:
            print(f"Error: The job name '{job_name}' already exists. Please use a different job name.")
            raise e

    def get_transcription_status(self, job_name):
        response = self.transcribe.get_transcription_job(TranscriptionJobName=job_name)
        return response['TranscriptionJob']['TranscriptionJobStatus']
    
    def get_transcription_result(self, job_name):
        response = self.transcribe.get_transcription_job(TranscriptionJobName=job_name)
        return response['TranscriptionJob']['Transcript']['TranscriptFileUri']