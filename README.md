# transcription-tool
Automating transcriptions for PKM/RAG

## Directory Structure
```
transcription-tool/
│
├── input/                # Folder for input files
├── output/               # Folder for output files
├── transcription_tool/   # Main package
│   ├── __init__.py
│   ├── s3_manager.py
│   ├── transcribe_manager.py
│   ├── file_manager.py
│   └── transcription_tool.py
├── .env                  # Environment variables
├── requirements.txt      # Dependencies
└── main.py               # Entry point to kick off the script
```

## Setup

### Configuring your s3 bucket policy

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