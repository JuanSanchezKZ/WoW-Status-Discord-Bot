import requests
from dotenv import load_dotenv
import os

load_dotenv()

getURL = os.getenv("API_URL")


def get_status():
  r = requests.get(url = getURL)
  data = r.json()

  status = data.get('status').get('name')


  if status == "Down":
        return "El servidor está caído"
  else:
        return "Ya se puede ingresar al servidor."
    
 

