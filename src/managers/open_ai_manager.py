from time import sleep

from openai import OpenAI
from pathlib import Path


from ..configs.formatting_config import OPEN_AI_API_KEY, OPEN_AI_ASSISTANT_ID

class OpenAiManager():
    def __init__(self):
        self.open_ai = OpenAI(
            api_key=OPEN_AI_API_KEY
        )
        self.file_id = None
        self.thread_id = None
        self.run_id = None

    def upload_file(self, file_path):
        response = self.open_ai.files.create(
            file=Path(file_path),
            purpose='user_data',
        )
        self.file_id = response.id

    def create_thread(self):
        thread = self.open_ai.beta.threads.create(
        )
        self.thread_id = thread.id

    def create_message(self):
        self.open_ai.beta.threads.messages.create(
            content="format the transcript.",
            thread_id=self.thread_id,
            role="user",
            attachments=[{"file_id": self.file_id, "tools": [{"type": "file_search"}]}]
        )

    def run_thread(self):
        if not self.thread_id:
            raise ValueError("Thread ID is not set. Create a thread first.")
        
        run = self.open_ai.beta.threads.runs.create(
            thread_id=self.thread_id,
            assistant_id=OPEN_AI_ASSISTANT_ID
        )

        self.run_id = run.id
    
    def wait_for_run(self):
        if self.run_id == None: 
            raise "You need to create a run first!"
        
        while True:
            print("Running thread...")
            run = self.open_ai.beta.threads.runs.retrieve(
                run_id=self.run_id,
                thread_id=self.thread_id
            )
            status = run.status
            if status in ['queued', 'in_progress']:
                sleep(3)
            elif status in ['completed']:
                return
            else:
                raise "There was a problem with the run"
    
    def format_transcript(self):
        self.create_thread()
        thread = self.open_ai.beta.threads.create(
            assistant_id=OPEN_AI_ASSISTANT_ID
        )
        # Get the response from the assistant
        response = self.open_ai.beta.threads.run(thread.id)
        return response.messages[-1].content.strip()
    
    def get_response(self):
        response = self.open_ai.beta.threads.messages.list(
            thread_id=self.thread_id
        )
        return response.data[0].content[0].text.value

    def delete_file(self, file_id):
        self.open_ai.files.delete(file_id=file_id)