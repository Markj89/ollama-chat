import os
import requests
from requests.exceptions import RequestException
from ollama import Client
from dotenv import load_dotenv

load_dotenv()

def check_url(url) -> bool:
    try:
        response = requests.get(url, allow_redirects=True, timeout=5)
        response.raise_for_status()
        return True
    except RequestException:
        return False
    
def ollama_client(url) -> Client:
    return Client(
        host=url,
        headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY')}
    )
