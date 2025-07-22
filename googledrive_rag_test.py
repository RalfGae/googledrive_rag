from openai import OpenAI
from dotenv import load_dotenv
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

# Get the Google Drive OAuth credentials path from environment variables
credentials_path = os.getenv("GOOGLE_DRIVE_OAUTH_PATH")

# Google Drive API access setup
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

# client = OpenAI()

def main():
    #specify Folder-ID to search in Google Drive
    folder_id = os.getenv("GOOGLE_DRIVE_FOLDER_ID")

    # Authenticate with Google Drive
    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
    creds = flow.run_local_server(port=0)

    # Build the Google Drive service
    drive_service = build('drive', 'v3', credentials=creds)

    # List files in Google Drive (for demonstration purposes)
    results = drive_service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(f"{item['name']} ({item['id']})")

# def chat_loop():
#     current_response_id = None
# 
#     while True:
#         # Get user input
#         user_input = input("You: ")
# 
#         if user_input.lower() in ["exit", "bye", "quit"]:
#             print("Goodbye!")
#             break
# 
#         response = client.responses.create(
#             model="gpt-4o-mini",
#             input=user_input,
#             previous_response_id=current_response_id
#         )
# 
#         current_response_id = response.id
# 
#         # Print the response
#         print("Bot: ", response.output_text)

if __name__ == "__main__":
    main()
    #chat_loop()
