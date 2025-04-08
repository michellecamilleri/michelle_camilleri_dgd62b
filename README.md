# Task 1: Environment Setup and Technology Selection

1. Project setup
- Created the project folder

2. Created a virtual environment
- Created a virtual environment 
by using	'python – m venv env'
- Activated the environment 
by using	'env\Scripts\activate'

3. Installed necessary packages
- Python 3.11
- Fastapi - pip install fastapi
- Uvicorn – pip install uvicorn
- Motor – pip install motor
- Pydantic – pip install pydantic
- Python-dotenv – pip install python-dotenv
- Requests – pip install requests 

by using	'pip install fastapi uvicorn motor pydantic python-dotenv requests'

4. Generated Requirements File 
- by using	'pip freeze > requirements.txt'
   
5. Created the API using FastAPI
- Created a file called main.py
- Appended code from Appendix B
- Launch the FastAPI
by using	'uvicorn main:app –reload'
- Ensured the server was running by checking it's accessible through 'http://127.0.0.1:8000/docs'

6. Created a Git Repository Initialization
- Created a new private, local Git repository 
- Committed all files and folders
- Push manually though the GitHub desktop application
