from dotenv import load_dotenv
load_dotenv()
import os

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
GROUP_ID = os.getenv('GROUP_ID')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')