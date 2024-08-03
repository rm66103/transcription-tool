import boto3
from botocore.exceptions import ClientError

class S3Manager:
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        self.bucket_name = bucket_name

    def upload_file(self, file_path, object_name):
        try:
            self.s3.upload_file(file_path, self.bucket_name, object_name)
            print(f"Successfully uploaded {file_path} to {self.bucket_name}/{object_name}")
        except ClientError as e:
            print(f"Failed to upload {file_path} to {self.bucket_name}/{object_name}: {e}")
            raise

    def download_file(self, object_name, file_path):
        try:
            self.s3.download_file(self.bucket_name, object_name, file_path)
            print(f"Successfully downloaded {object_name} to {file_path}")
        except ClientError as e:
            print(f"Failed to download {object_name} from {self.bucket_name}: {e}")
            raise