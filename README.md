# ai-feedback

## It Works!

[Click to watch it in action](https://www.youtube.com/watch?v=shqL5b2Y-pM)

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


## Running the App

1) `flask --app app run` to run the app
2) Go to `https://http://localhost:5000/` in your browser
3) Verify it works!

## Unit Testing

There are two files - `test_routes` should be used to test the `app.py` file; `test_js_script` can be used to test the Javascript functions. It uses QuickJS to simulate a DOM.

1) Run `pytest -v` in the project folder
    - **BE CAREFUL** - the Python it makes actual API calls to Gemini, which costs you $$$ with your API key
