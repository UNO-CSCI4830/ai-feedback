# ai-feedback

## Setup Instructions

1) Clone the repo
2) Make sure Python is installed
3) Open a command line
4) Set a virtual environment
    - Example: `python -m venv .venv`
5) Activate it
    - Bash/Git: `source .venv/bin/activate`
    - Powershell: `.\.venv\Scripts\Activate`
    - (you should see `(.venv)` in front of the terminal line)
6) `pip install -r requirements.txt` to install the necessary packages
7) Create a file called `.env`
    - Bash/Git: `touch .env`
8) Add your Gemini API Key as `GEMINI_KEY=${key}`
    - Double-check that this file is being successfully ignored by the `.gitignore` file
8) `flask --app app run` to run the app