import os
from dotenv import load_dotenv

load_dotenv()

NAME = os.getenv('NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
SECRET_KEY = os.getenv('SECRET_KEY')
