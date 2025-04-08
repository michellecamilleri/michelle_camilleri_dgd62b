Task 1: Environment Setup and Technology Selection

Project setup
- Created the project folder


Created a virtual environment
- Created a virtual environment 
by using	'python – m venv env'
- Activated the environment 
by using	'env\Scripts\activate'


Installed necessary packages
- Python 3.11
- Fastapi - pip install fastapi
- Uvicorn – pip install uvicorn
- Motor – pip install motor
- Pydantic – pip install pydantic
- Python-dotenv – pip install python-dotenv
- Requests – pip install requests 

by using	'pip install fastapi uvicorn motor pydantic python-dotenv requests'


Generated Requirements File 
- by using	'pip freeze > requirements.txt'
   

Created the API using FastAPI
- Created a file called main.py
- Appended code from Appendix B
- Launch the FastAPI
by using	'uvicorn main:app –reload'
- Ensured the server was running by checking it's accessible through 'http://127.0.0.1:8000/docs'


Created a Git Repository Initialization
- Created a new private, local Git repository 
- Committed all files and folders
- Push manually though the GitHub desktop application
