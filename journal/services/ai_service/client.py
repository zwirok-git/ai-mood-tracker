import os
from groq import Groq

from dotenv import load_dotenv

load_dotenv()

CLIENT = Groq(api_key=os.environ.get("GROQ_API_KEY"))

