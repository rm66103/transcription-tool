# transcription-tool
Automating transcriptions for PKM/RAG
- Generate transcripts from audio files
- Generate well formatted transcripts for PKM/RAG
- Generate insights from transcripts for PKM/RAG 

## Directory Structure
```
transcription-tool/
│
├── input/                # Folder for input files
├── output/               # Folder for output files
│   ├── raw_transcripts/
│   ├── formatted_transcripts/
│   ├── transcript_notes/
├── src 
│   ├── ...               # Code
├── .env                  # Environment variables
├── requirements.txt      # Dependencies
├── transcribe.py         # Create transcripts from input/
└── format.py             # Format transcripts in raw_transcripts/
```

## Setup

You will need the following to use this project
- AWS S3 Bucket
- AWS IAM User
- Open AI API Key

### Configuring your IAM User Permissions
Assign permissions policies.
- `AmazonS3FullAccess`
- `AmazonTranscribeFullAccess`

### Configuring your IAM User Authentication
To allow your application to use the specified IAM user for accessing the S3 bucket, you need to configure the AWS SDK (e.g., Boto3 for Python) with the IAM user's credentials. Here are the steps to achieve this:

1. Create Access Keys for the IAM User:
- Go to the IAM service in the AWS Management Console.
- Select the IAM user transcript-tool-user.
- Go to the "Security credentials" tab.
- Click "Create access key" to generate a new access key and secret access key. Make sure to store these keys securely.

2. Configure AWS SDK with IAM User Credentials:
- You can configure the AWS SDK to use the IAM user's credentials in several ways, such as using environment variables, AWS credentials file, or directly in your code.

### Configuring your s3 bucket policy
Example bucket policy for uploading and downloading your audio and transcripts.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<YOUR_AWS_ACCOUNT_ID>:user/<YOUR_IAM_USER_NAME>"
            },
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::<YOUR_BUCKET_NAME>/*"
        }
    ]
}
```

### Project Setup
1. create a folder called `input` in the top level of the project.
2. create a folder called `output` in the top level of the project.
3. create the foldeers `raw_transcripts`, `formatted_transcripts`, and `transcript_notes` in the `output` forlder

### Environment Setup
1. Install the requirements.
```bash
pip install -r requirements.txt
```
2. Set your environment variables. Use `.env.template` to see what values you will need.

### Running the project
1. Add your audio files in to the `input` folder.
2 Run the script.
```bash
# Create transcriptions
python transcribe.py

# Create transcriptions with multiple speakers
python transcribe.py --speaker_count=5

# Format the transcripts
python format.py

# Clear your input and output folders
bash clear_folders.sh
```

## To Do
- [ ] Cleanup AWS s3 buckets, AWS transcribe jobs, and OpenAI API Threads after use.
- [ ] Add script to summarize and gain insights from transcripts.