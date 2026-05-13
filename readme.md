## Installation Steps

- Ran the command: `pip3 install virtualenv`
- Ran the command: `virtualenv venv`
  - This creates a virtual environment for the project
- Ran the command: `source env/bin/activate`
  - After running this command, `(env)` is shown in the terminal
- Now install FastAPI: `pip3 install fastapi`
- Now install Uvicorn to run and test the API: `pip3 install uvicorn`

## Running the App

- To run the app, run the command: `uvicorn main:app --reload`
