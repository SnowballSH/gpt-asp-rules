from dotenv import load_dotenv
import os

load_dotenv()

# Enter your GPT-3 API key here
API_KEY = os.getenv('OPENAI_API_KEY')
# [optional] you may also put your ORG key below
ORG_KEY = ''