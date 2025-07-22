# DummyEnv
DummyEnv: Quick AI Project Starter

## Overview
This repository provides a simple terminal-based script using Googledrives's API. It is designed for fast setup and experimentation with Googledrive API for file storage.

## Features
- Test script for Googledrive connection and file summary of specific folder
- Easy setup with a shell script
- Uses environment variables for API keys

## Files
- `googledrive_rag_test.py`: Main script
- `requirements.txt`: Python dependencies
- `setup.sh`: Setup script for virtual environment and dependencies

## Setup
1. **Clone this repository**
2. **Run the setup script:**
   ```bash
   bash setup.sh
   ```
3. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```
4. **Set up your environment variables:**
   - Create a `.env` file in the project root with:
     ```
     OPENAI_API_KEY=your-api-key-here
     GOOGLE_DRIVE_OAUTH_PATH=creds/your_oauth_credentials.json
     GOOGLE_DRIVE_FOLDER_ID=your-google-drive-folder-id
     ```

## Usage
Run the chatbot:
```bash
python3 googledrive_rag_test.py
```
Type your message and interact with the bot. Type `exit`, `bye`, or `quit` to end the session. The bot can answer questions about files in your specified Google Drive folder.

## Dependencies
- annotated-types
- anyio
- cachetools
- certifi
- charset-normalizer
- distro
- google-api-core
- google-api-python-client
- google-auth
- google-auth-httplib2
- google-auth-oauthlib
- googleapis-common-protos
- h11
- httpcore
- httplib2
- httpx
- idna
- jiter
- oauthlib
- openai
- proto-plus
- protobuf
- pyasn1
- pyasn1_modules
- pydantic
- pydantic_core
- pyparsing
- python-dotenv
- requests
- requests-oauthlib
- rsa
- sniffio
- tqdm
- typing-inspection
- typing_extensions
- uritemplate
- urllib3

## License
MIT (or specify your license)
