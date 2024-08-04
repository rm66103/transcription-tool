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
- Open AI Assistant

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

### Configuring your Open AI Assistant
I used the OpenAI playground to generate the assistant.

You will need to give a set of instructions to your assistant.

Here are the instructions I use (20240804)

```
Context: I have a transcript of a conversation and I need a comprehensive analysis to extract key insights.

Instructions:

1. Events:
   - Identify any events discussed in the conversation.
   - For each event, provide details on:
     - What is happening?
     - When and where is the event happening?
     - Who else will be there?
     - Any other helpful details for attendees of the event.

2. Speaker Information:
   - For each speaker in the conversation, gather the following information:
     - Likes or dislikes
     - Where they are from
     - What they do for work
     - Who they are dating
     - Any goals they have
     - Things they are working on
     - Personality traits or values revealed in the conversation
     - life stories
     - Other random details or information
   - Use the transcript to paint a detailed picture of each speaker.

3. Conversation Summary:
   - Provide a brief summary of the entire conversation.

If there is not enough context for a specific insight, then do not guess. Simply omit it. Do not infer anything. Only generate insights based on what is being said.
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

# Get insights from formatted transcripts
python insights.py

# Clear your input and output folders
bash clear_folders.sh
```

## To Do
- [ ] Customize insights based on transcript type (conversation, sermon, podcast)