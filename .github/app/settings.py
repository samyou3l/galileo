# settings.py
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.environ['FRED_API_KEY']
#ROOT = os.path.dirname(os.path.realpath(__file__))
